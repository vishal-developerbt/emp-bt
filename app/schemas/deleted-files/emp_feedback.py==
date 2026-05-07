from pydantic import BaseModel, ConfigDict
from typing import Optional


class FeedbackCreate(BaseModel):
    user_id: int
    reviewer_id: int
    message: Optional[str]
    status: Optional[bool] = True


class FeedbackUpdate(BaseModel):
    message: Optional[str]
    status: Optional[bool]


class FeedbackResponse(BaseModel):
    id: int
    user_id: int
    reviewer_id: int
    message: Optional[str]
    status: bool

    model_config = ConfigDict(from_attributes=True)