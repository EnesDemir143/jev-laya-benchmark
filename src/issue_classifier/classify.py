from typesafe_sdk import AsyncTypeSafeClient, Choice, Noul

from issue_classifier.io import label_names
from issue_classifier.models import ClassifiedIssue, Classification, IssueRecord
from issue_classifier.prompt import (
    BEGINNER_CRITERIA,
    BEGINNER_INSTRUCTIONS,
    CV_FIT_CRITERIA,
    CV_FIT_INSTRUCTIONS,
    DIFFICULTY_CRITERIA,
    DIFFICULTY_INSTRUCTIONS,
    issue_state,
)
from issue_classifier.settings import Settings

QUESTIONS = {
    "beginner_friendly": Noul(
        instructions=BEGINNER_INSTRUCTIONS,
        criteria=BEGINNER_CRITERIA,
    ),
    "cv_fit": Noul(
        instructions=CV_FIT_INSTRUCTIONS,
        criteria=CV_FIT_CRITERIA,
    ),
    "difficulty": Choice(
        instructions=DIFFICULTY_INSTRUCTIONS,
        criteria=DIFFICULTY_CRITERIA,
    ),
}


def make_client(settings: Settings) -> AsyncTypeSafeClient:
    kwargs: dict = {
        "api_key": settings.typesafe_api_key.get_secret_value(),
        "model": settings.typesafe_default_model,
        "timeout": settings.typesafe_timeout,
    }
    if settings.typesafe_base_url:
        kwargs["base_url"] = settings.typesafe_base_url
    return AsyncTypeSafeClient(**kwargs)


async def classify_issue(
    client: AsyncTypeSafeClient,
    resume: str,
    issue: IssueRecord,
    *,
    threshold: float,
) -> Classification:
    result = await client.system_one(
        state=issue_state(resume, issue),
        questions=QUESTIONS,
    )
    beginner = result.nouls["beginner_friendly"].noul
    cv_fit = result.nouls["cv_fit"].noul
    difficulty_answer = result.choices["difficulty"]
    difficulty = difficulty_answer.choice
    if difficulty not in ("easy", "mid", "hard"):
        raise ValueError(f"unexpected difficulty choice: {difficulty!r}")
    return Classification(
        beginner_friendly=beginner >= threshold,
        beginner_friendly_noul=beginner,
        cv_fit=cv_fit >= threshold,
        cv_fit_noul=cv_fit,
        difficulty=difficulty,
        difficulty_confidence=difficulty_answer.confidence,
        difficulty_probabilities=dict(difficulty_answer.probabilities),
    )


async def classify_or_error(
    client: AsyncTypeSafeClient,
    resume: str,
    issue: IssueRecord,
    *,
    threshold: float,
) -> ClassifiedIssue:
    base = ClassifiedIssue(
        number=issue.number,
        title=issue.title,
        url=issue.url,
        labels=label_names(issue),
    )
    try:
        classified = await classify_issue(client, resume, issue, threshold=threshold)
    except Exception as exc:  # noqa: BLE001 — keep the batch running
        base.error = f"{type(exc).__name__}: {exc}"
        return base
    return base.model_copy(update=classified.model_dump())
