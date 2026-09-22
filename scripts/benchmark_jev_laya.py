"""Compare Jev and laya-mlx on the same issue sample."""
from __future__ import annotations
import argparse, asyncio, json, statistics, time
from pathlib import Path
from typing import Any
from issue_classifier.classify import QUESTIONS, classify_or_error, make_client
from issue_classifier.io import load_issues, load_resume
from issue_classifier.prompt import issue_state
from issue_classifier.settings import Settings
ROOT = Path(__file__).resolve().parents[1]

def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--limit", type=int, default=100)
    p.add_argument("--input", type=Path, default=ROOT / "data/oh-my-pi-open-issues.json")
    p.add_argument("--resume", type=Path, required=True)
    p.add_argument("--output", type=Path, default=ROOT / "data/jev-laya-benchmark.json")
    p.add_argument("--laya-model", default="aac6fef/laya-mlx")
    p.add_argument("--dtype", choices=("float16", "float32"), default="float32")
    p.add_argument("--batch-size", type=int, default=16)
    return p.parse_args()

def questions() -> dict[str, Any]:
    return {
        "beginner_friendly": {"type": "noul", "instructions": QUESTIONS["beginner_friendly"].instructions, "criteria": QUESTIONS["beginner_friendly"].criteria},
        "cv_fit": {"type": "noul", "instructions": QUESTIONS["cv_fit"].instructions, "criteria": QUESTIONS["cv_fit"].criteria},
        "difficulty": {"type": "choice", "instructions": QUESTIONS["difficulty"].instructions, "criteria": list(QUESTIONS["difficulty"].criteria)},
    }

def laya_row(result: dict[str, Any], elapsed: float) -> dict[str, Any]:
    a = result["answers"]
    b, c, d = (a[k] for k in ("beginner_friendly", "cv_fit", "difficulty"))
    return {"beginner_friendly": b["noul"] >= .5, "beginner_friendly_noul": b["noul"], "beginner_friendly_confidence": b["confidence"], "cv_fit": c["noul"] >= .5, "cv_fit_noul": c["noul"], "cv_fit_confidence": c["confidence"], "difficulty": d["choice"], "difficulty_confidence": d["confidence"], "difficulty_probabilities": d["probabilities"], "elapsed_ms": round(elapsed, 3)}

def pct(values: list[float], p: float) -> float:
    values = sorted(values)
    return values[min(len(values)-1, round((len(values)-1)*p))]

def summary(records):
    ok = [
        r for r in records
        if not r["jev"].get("error") and not r["laya"].get("error")
    ]
    timed = ok
    print(f"issues: {len(records)} (successful on both: {len(ok)})")
    for name in ("jev", "laya"):
        t = [r[name]["elapsed_ms"] for r in timed]
        if t: print(f"{name:5} mean={statistics.mean(t):.1f}ms p50={pct(t,.5):.1f}ms p95={pct(t,.95):.1f}ms")
    for field in ("beginner_friendly", "cv_fit", "difficulty"):
        if timed:
            same = sum(r["jev"].get(field) == r["laya"].get(field) for r in timed)
            print(f"{field:20} agreement={same}/{len(timed)} ({same/len(timed):.1%})")
    for field in ("beginner_friendly_noul", "cv_fit_noul"):
        d = [abs(r["jev"][field]-r["laya"][field]) for r in timed]
        if d: print(f"{field:20} mean_abs_diff={statistics.mean(d):.4f} max={max(d):.4f}")

async def run(args):
    import laya_mlx as laya

    if args.limit < 1: raise ValueError("--limit must be positive")
    issues, resume, qs = load_issues(args.input)[:args.limit], load_resume(args.resume), questions()
    settings, agent, records = Settings(), laya.load(args.laya_model, dtype=args.dtype, batch_size=args.batch_size), []
    warmup_state = issue_state(resume, issues[0])
    agent.predict(warmup_state, qs)
    async with make_client(settings) as client:
        for i, issue in enumerate(issues, 1):
            started = time.perf_counter()
            jev = await classify_or_error(client, resume, issue, threshold=settings.noul_threshold)
            jev_ms = (time.perf_counter()-started)*1000
            started = time.perf_counter()
            try: laya_data = laya_row(agent.predict(issue_state(resume, issue), qs), (time.perf_counter()-started)*1000)
            except Exception as exc: laya_data = {"error": f"{type(exc).__name__}: {exc}"}
            records.append({"number": issue.number, "title": issue.title,
                            "jev": {**jev.model_dump(mode="json"), "elapsed_ms": round(jev_ms,3)},
                            "laya": laya_data})
            print(f"[{i:3}/{len(issues)}] #{issue.number} Jev={jev_ms:.1f}ms Laya={laya_data.get('elapsed_ms',0):.1f}ms")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({"config": vars(args) | {"input": str(args.input), "resume": str(args.resume)}, "records": records}, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    summary(records); print(f"raw results: {args.output}")

if __name__ == "__main__": raise SystemExit(asyncio.run(run(parse_args())))
