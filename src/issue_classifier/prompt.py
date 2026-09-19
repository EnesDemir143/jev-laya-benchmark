from issue_classifier.io import comment_excerpts, label_names
from issue_classifier.models import IssueRecord

BEGINNER_INSTRUCTIONS = (
    "Is this GitHub issue beginner-friendly for a new contributor to the "
    "oh-my-pi coding-agent CLI (TypeScript/Bun/TUI/MCP)? "
    "Judge primarily from `issue.body`, then title, labels, and comments."
)

BEGINNER_CRITERIA = {
    "true": (
        "A new contributor could reasonably start from the description: "
        "docs, small UI copy, isolated bug, well-scoped feature, or first-issue shape."
    ),
    "false": (
        "Needs deep product internals, RFC architecture, multi-package refactors, "
        "protocol/auth edge cases, or unclear scope."
    ),
}

CV_FIT_INSTRUCTIONS = (
    "Given `candidate_resume`, would this issue be a good match for this candidate "
    "to contribute to (skills, stack, and experience overlap with the work implied "
    "by `issue.body`, title, labels, and comments)?"
)

CV_FIT_CRITERIA = {
    "true": (
        "The resume's languages, tools, or domains clearly overlap with the issue "
        "(for example CLI/TUI, TypeScript, agents, APIs, or related systems work)."
    ),
    "false": (
        "The issue is outside the resume's demonstrated stack/domain, or the "
        "description does not show work that matches the resume."
    ),
}

DIFFICULTY_INSTRUCTIONS = (
    "Pick one difficulty for a contributor implementing or fixing this issue, "
    "using `issue.body` as the primary evidence, then title, labels, and comments."
)

DIFFICULTY_CRITERIA = {
    "easy": (
        "Narrow, local change: copy, small bug, docs, config flag, or well-described one-file fix."
    ),
    "mid": (
        "Requires reading several modules or a non-trivial but bounded feature/bug "
        "without rewriting core architecture."
    ),
    "hard": (
        "Architecture RFC, protocol/auth/runtime internals, large TUI/session machinery, "
        "or multi-system behavior that is hard to scope even with the description."
    ),
}


def issue_state(resume: str, issue: IssueRecord) -> dict:
    return {
        "candidate_resume": resume,
        "issue": {
            "number": issue.number,
            "title": issue.title,
            "url": issue.url,
            "state": issue.state,
            "body": issue.body or "",
            "labels": label_names(issue),
            "comment_count": len(issue.comments),
            "comment_excerpts": comment_excerpts(issue),
        },
        "data_notes": (
            "Prefer `issue.body` (the GitHub issue description). "
            "Use title, labels, and comment excerpts as supporting context. "
            "Do not invent a body if it is empty."
        ),
    }
