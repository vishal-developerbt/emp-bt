from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Dict, Any
from datetime import date, time


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

class BlockCreate(BaseModel):
    timesheet_date: date
    user_id: Optional[int] = 0
    is_block: Optional[bool] = True


class BlockUpdate(BaseModel):
    is_block: Optional[bool]


class BlockResponse(BaseModel):
    id: int
    timesheet_date: date
    is_block: bool
    user_id: int
    approved_by: Optional[int]

    model_config = ConfigDict(from_attributes=True)

class HolidayCreate(BaseModel):
    holiday_name: str
    date: date
    type: str
    status: Optional[bool] = True


class HolidayUpdate(BaseModel):
    holiday_name: Optional[str]
    date: Optional[date]
    type: Optional[str]
    status: Optional[bool]


class HolidayResponse(BaseModel):
    id: int
    holiday_name: str
    date: date
    type: str
    status: bool

    model_config = ConfigDict(from_attributes=True)