from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from issue_classifier.classify import classify_or_error, make_client
from issue_classifier.io import (
    load_classifications,
    load_issues,
    load_resume,
    pending_issues,
    write_classifications,
)
from issue_classifier.models import ClassifiedIssue, IssueRecord
from issue_classifier.rate_limit import AsyncRateLimiter
from issue_classifier.settings import Settings

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = ROOT / "data" / "oh-my-pi-open-issues.json"
DEFAULT_OUTPUT = ROOT / "data" / "oh-my-pi-issue-classifications.json"
DEFAULT_RESUME = ROOT / "resume.md"
DRY_RUN_LIMIT = 10


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Classify oh-my-pi GitHub issues with TypeSafe Jev (beginner / CV fit / difficulty)."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--resume", type=Path, default=DEFAULT_RESUME)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help=f"Classify only the first {DRY_RUN_LIMIT} issues (e2e smoke).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Max issues to classify. With --dry-run the cap is always at most 10 (min(limit, 10)).",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=None,
        help="Max in-flight TypeSafe requests (default: 8, or TYPESAFE_CONCURRENCY).",
    )
    parser.add_argument(
        "--rps",
        type=float,
        default=None,
        help="Max request starts per second (default: 15, cap 20).",
    )
    return parser


def resolve_limit(*, dry_run: bool, limit: int | None) -> int | None:
    if limit is not None and limit < 1:
        raise ValueError("--limit must be >= 1")
    if dry_run:
        if limit is None:
            return DRY_RUN_LIMIT
        return min(limit, DRY_RUN_LIMIT)
    return limit


def resolve_output(*, dry_run: bool, output: Path | None) -> Path:
    if output is not None:
        return output
    if dry_run:
        return ROOT / "data" / "oh-my-pi-issue-classifications.dry-run.json"
    return DEFAULT_OUTPUT


def _fmt_prob(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.4f}"


def format_row(index: int, total: int, row: ClassifiedIssue, *, threshold: float) -> str:
    title = row.title.replace("\n", " ").strip()
    if len(title) > 90:
        title = title[:87] + "..."
    header = f"[{index}/{total}] #{row.number}  {title}"
    if row.error:
        return f"{header}\n  error: {row.error}"

    beginner = "yes" if row.beginner_friendly else "no"
    cv_fit = "yes" if row.cv_fit else "no"
    probs = row.difficulty_probabilities or {}
    ordered = [k for k in ("easy", "mid", "hard") if k in probs]
    ordered.extend(sorted(k for k in probs if k not in ordered))
    p_line = "  ".join(f"P({name})={_fmt_prob(probs[name])}" for name in ordered) or "n/a"

    return (
        f"{header}\n"
        f"  beginner_friendly  {beginner:3}  noul={_fmt_prob(row.beginner_friendly_noul)}"
        f"  (P(yes); threshold={threshold:g})\n"
        f"  cv_fit             {cv_fit:3}  noul={_fmt_prob(row.cv_fit_noul)}"
        f"  (P(yes); threshold={threshold:g})\n"
        f"  difficulty         {row.difficulty}  confidence={_fmt_prob(row.difficulty_confidence)}\n"
        f"    {p_line}"
    )


def _merge_rows(
    existing: list[ClassifiedIssue],
    todo: list[IssueRecord],
    completed: dict[int, ClassifiedIssue],
) -> list[ClassifiedIssue]:
    return existing + [completed[issue.number] for issue in todo if issue.number in completed]


async def _classify_batch(
    *,
    settings: Settings,
    resume: str,
    existing: list[ClassifiedIssue],
    todo: list[IssueRecord],
    output: Path,
    concurrency: int,
    rps: float,
) -> list[ClassifiedIssue]:
    limiter = AsyncRateLimiter(rps)
    semaphore = asyncio.Semaphore(concurrency)
    completed: dict[int, ClassifiedIssue] = {}
    write_lock = asyncio.Lock()
    total = len(todo)

    async with make_client(settings) as client:

        async def worker(issue: IssueRecord) -> None:
            async with semaphore:
                await limiter.acquire()
                row = await classify_or_error(
                    client,
                    resume,
                    issue,
                    threshold=settings.noul_threshold,
                )
            async with write_lock:
                completed[issue.number] = row
                rows = _merge_rows(existing, todo, completed)
                write_classifications(output, rows)
                print(
                    format_row(
                        len(completed),
                        total,
                        row,
                        threshold=settings.noul_threshold,
                    )
                )
                print()

        await asyncio.gather(*(worker(issue) for issue in todo))

    return _merge_rows(existing, todo, completed)


def run(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    limit = resolve_limit(dry_run=args.dry_run, limit=args.limit)
    output = resolve_output(dry_run=args.dry_run, output=args.output)

    settings = Settings()
    concurrency = args.concurrency if args.concurrency is not None else settings.typesafe_concurrency
    rps = args.rps if args.rps is not None else settings.typesafe_requests_per_second
    if concurrency < 1 or concurrency > 32:
        raise ValueError("--concurrency must be between 1 and 32")
    if rps <= 0 or rps > 20:
        raise ValueError("--rps must be in (0, 20]")

    issues = load_issues(args.input)
    if limit is not None:
        issues = issues[:limit]
    resume = load_resume(args.resume)

    existing = load_classifications(output)
    todo = pending_issues(issues, existing)
    print(
        f"{len(existing)} already in {output}; "
        f"classifying {len(todo)} remaining of {len(issues)} "
        f"(concurrency={concurrency}, rps={rps:g})"
    )
    print()
    if not todo:
        errors = sum(1 for row in existing if row.error)
        print(f"nothing to do ({errors} error(s) already recorded)")
        return 1 if errors else 0

    rows = asyncio.run(
        _classify_batch(
            settings=settings,
            resume=resume,
            existing=existing,
            todo=todo,
            output=output,
            concurrency=concurrency,
            rps=rps,
        )
    )
    errors = sum(1 for row in rows if row.error)
    print(f"wrote {len(rows)} rows ({errors} error(s)) to {output}")
    return 1 if errors else 0
