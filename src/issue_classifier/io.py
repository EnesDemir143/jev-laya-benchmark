from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

from issue_classifier.models import ClassifiedIssue, IssueRecord

_COMMENT_EXCERPT_LIMIT = 3
_COMMENT_CHAR_LIMIT = 400


def load_issues(path: Path) -> list[IssueRecord]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError(f"Expected a JSON array of issues in {path}")
    return [IssueRecord.model_validate(item) for item in raw]


def load_resume(path: Path) -> str:
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError(f"Resume file is empty: {path}")
    return text


def label_names(issue: IssueRecord) -> list[str]:
    names: list[str] = []
    for label in issue.labels:
        if isinstance(label, str):
            names.append(label)
        elif isinstance(label, dict) and label.get("name"):
            names.append(str(label["name"]))
    return names


def comment_excerpts(issue: IssueRecord) -> list[str]:
    excerpts: list[str] = []
    for comment in issue.comments[:_COMMENT_EXCERPT_LIMIT]:
        if isinstance(comment, dict):
            body = str(comment.get("body") or "").strip()
        else:
            body = str(comment).strip()
        if not body:
            continue
        if len(body) > _COMMENT_CHAR_LIMIT:
            body = body[:_COMMENT_CHAR_LIMIT] + "…"
        excerpts.append(body)
    return excerpts


def load_classifications(path: Path) -> list[ClassifiedIssue]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError(f"Expected a JSON array of classifications in {path}")
    return [ClassifiedIssue.model_validate(item) for item in raw]


def pending_issues(
    issues: list[IssueRecord],
    existing: list[ClassifiedIssue],
) -> list[IssueRecord]:
    done = {row.number for row in existing}
    return [issue for issue in issues if issue.number not in done]


def write_classifications(path: Path, rows: list[ClassifiedIssue]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(
        [row.model_dump(mode="json") for row in rows],
        indent=2,
        ensure_ascii=False,
    ) + "\n"
    fd, tmp_name = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=path.parent,
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise
