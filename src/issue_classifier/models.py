from typing import Any, Literal

from pydantic import BaseModel, Field

Difficulty = Literal["easy", "mid", "hard"]


class IssueRecord(BaseModel):
    number: int
    title: str
    url: str
    state: str = "OPEN"
    labels: list[Any] = Field(default_factory=list)
    comments: list[Any] = Field(default_factory=list)
    body: str | None = None
    author: Any | None = None
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")

    model_config = {"populate_by_name": True}


class Classification(BaseModel):
    beginner_friendly: bool
    beginner_friendly_noul: float
    cv_fit: bool
    cv_fit_noul: float
    difficulty: Difficulty
    difficulty_confidence: float
    difficulty_probabilities: dict[str, float] = Field(default_factory=dict)


class ClassifiedIssue(BaseModel):
    number: int
    title: str
    url: str
    labels: list[str] = Field(default_factory=list)
    beginner_friendly: bool | None = None
    cv_fit: bool | None = None
    difficulty: Difficulty | None = None
    beginner_friendly_noul: float | None = None
    cv_fit_noul: float | None = None
    difficulty_confidence: float | None = None
    difficulty_probabilities: dict[str, float] | None = None
    error: str | None = None
