from pydantic import BaseModel, ConfigDict
from typing import Optional


class EmpShiftCreate(BaseModel):
    shift_name: Optional[str]
    timezone: Optional[str]
    shift_start_time: str
    logged_in_by: str
    status: Optional[str] = "Enable"


class EmpShiftUpdate(BaseModel):
    shift_name: Optional[str]
    timezone: Optional[str]
    shift_start_time: Optional[str]
    logged_in_by: Optional[str]
    status: Optional[str]


class EmpShiftResponse(BaseModel):
    id: int
    shift_name: Optional[str]
    timezone: Optional[str]
    shift_start_time: str
    logged_in_by: str
    status: str

    model_config = ConfigDict(from_attributes=True)