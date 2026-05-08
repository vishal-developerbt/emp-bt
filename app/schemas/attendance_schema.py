from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import date
from enum import Enum


class StatusEnum(str, Enum):
    Pending = "Pending"
    Approved = "Approved"
    Reject = "Reject"
    ReferBack = "ReferBack"


# ---------------- TIMESHEET ---------------- #

class TimesheetCreate(BaseModel):
    project_id: int
    user_id: int
    manager_id: Optional[int] = None
    hours: int = Field(ge=0, le=24)
    minutes: int = Field(ge=0, le=59)
    select_date: date
    description: Optional[str] = None


class TimesheetUpdate(BaseModel):
    project_id: Optional[int] = None
    hours: Optional[int] = Field(default=None, ge=0, le=24)
    minutes: Optional[int] = Field(default=None, ge=0, le=59)
    select_date: Optional[date] = None
    description: Optional[str] = None


class TimesheetStatusUpdate(BaseModel):
    status: StatusEnum
    manager_comment: Optional[str] = None


class TimesheetResponse(BaseModel):
    id: int
    project_id: int
    user_id: int
    manager_id: Optional[int]
    hours: int
    minutes: int
    select_date: date
    description: Optional[str]
    status: StatusEnum
    manager_comment: Optional[str]
    model_config = ConfigDict(from_attributes=True)


# ---------------- TIMESHEET COMMENTS ---------------- #

class TimesheetCommentCreate(BaseModel):
    timesheet_id: int
    comment_history: Optional[str] = None
    status: StatusEnum = StatusEnum.Pending


class TimesheetCommentUpdate(BaseModel):
    comment_history: Optional[str] = None
    status: Optional[StatusEnum] = None


class TimesheetCommentResponse(BaseModel):
    id: int
    timesheet_id: int
    comment_history: Optional[str]
    status: StatusEnum
    model_config = ConfigDict(from_attributes=True)


# ---------------- BLOCK TIMESHEET ---------------- #

class BlockCreate(BaseModel):
    timesheet_date: date
    user_id: Optional[int] = 0
    is_block: Optional[bool] = True


class BlockUpdate(BaseModel):
    is_block: Optional[bool] = None


class BlockResponse(BaseModel):
    id: int
    timesheet_date: date
    is_block: bool
    user_id: int
    approved_by: Optional[int]
    model_config = ConfigDict(from_attributes=True)


# ---------------- HOLIDAY ---------------- #

class HolidayCreate(BaseModel):
    holiday_name: str
    date: date
    holiday_type: str
    status: Optional[bool] = True


class HolidayUpdate(BaseModel):
    holiday_name: Optional[str] = None
    date: Optional[date] = None
    holiday_type: Optional[str] = None
    status: Optional[bool] = None


class HolidayResponse(BaseModel):
    id: int
    holiday_name: str
    date: date
    holiday_type: str
    status: bool
    model_config = ConfigDict(from_attributes=True)