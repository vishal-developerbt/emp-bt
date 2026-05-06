from pydantic import BaseModel, ConfigDict
from typing import Optional


class TimesheetCommentCreate(BaseModel):
    timesheet_id: int
    comment_history: Optional[str]
    status: Optional[str] = "Pending"


class TimesheetCommentUpdate(BaseModel):
    comment_history: Optional[str]
    status: Optional[str]


class TimesheetCommentResponse(BaseModel):
    id: int
    timesheet_id: int
    comment_history: Optional[str]
    status: str

    model_config = ConfigDict(from_attributes=True)