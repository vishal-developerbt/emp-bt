from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date


class TimesheetCreate(BaseModel):
    project_id: int
    user_id: int
    manager_id: Optional[int]
    hours: str
    minutes: str
    select_date: date
    description: Optional[str]


class TimesheetUpdate(BaseModel):
    project_id: Optional[int]
    hours: Optional[str]
    minutes: Optional[str]
    select_date: Optional[date]
    description: Optional[str]


class TimesheetStatusUpdate(BaseModel):
    status: str
    manager_comment: Optional[str]


class TimesheetResponse(BaseModel):
    id: int
    project_id: int
    user_id: int
    manager_id: Optional[int]
    hours: str
    minutes: str
    select_date: date
    description: Optional[str]
    status: str
    manager_comment: Optional[str]

    model_config = ConfigDict(from_attributes=True)