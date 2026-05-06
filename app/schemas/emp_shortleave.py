from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date


class ShortLeaveCreate(BaseModel):
    user_id: int
    start_date: date
    end_date: date
    partical_leave: Optional[str]
    project_manager: str
    approved_by: Optional[int]
    cc: Optional[str]
    leave_count: int
    message: Optional[str]
    status: Optional[int] = 0


class ShortLeaveUpdate(BaseModel):
    start_date: Optional[date]
    end_date: Optional[date]
    partical_leave: Optional[str]
    project_manager: Optional[str]
    approved_by: Optional[int]
    cc: Optional[str]
    leave_count: Optional[int]
    message: Optional[str]
    status: Optional[int]
    comment: Optional[str]


class ShortLeaveResponse(BaseModel):
    id: int
    user_id: int
    start_date: date
    end_date: date
    partical_leave: Optional[str]
    project_manager: str
    approved_by: Optional[int]
    cc: Optional[str]
    leave_count: int
    message: Optional[str]
    status: int
    comment: Optional[str]

    model_config = ConfigDict(from_attributes=True)