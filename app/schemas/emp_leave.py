from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date


class LeaveCreate(BaseModel):
    user_id: int
    start_date: date
    end_date: date
    partical_leave: Optional[str]
    leave_type: str
    project_manager: str
    approved_by: Optional[int]
    applied_by: int
    cc: Optional[str]
    leave_count: float
    message: Optional[str]


class LeaveUpdate(BaseModel):
    start_date: Optional[date]
    end_date: Optional[date]
    partical_leave: Optional[str]
    leave_type: Optional[str]
    project_manager: Optional[str]
    approved_by: Optional[int]
    cc: Optional[str]
    leave_count: Optional[float]
    message: Optional[str]
    status: Optional[int]


class LeaveResponse(BaseModel):
    id: int
    user_id: int
    start_date: date
    end_date: date
    partical_leave: Optional[str]
    leave_type: str
    project_manager: str
    approved_by: Optional[int]
    applied_by: int
    cc: Optional[str]
    leave_count: float
    message: Optional[str]
    status: int

    model_config = ConfigDict(from_attributes=True)