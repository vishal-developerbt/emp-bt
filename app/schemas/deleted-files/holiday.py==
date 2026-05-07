from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date


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