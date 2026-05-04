from pydantic import BaseModel
from datetime import date


class HolidayCreate(BaseModel):
    name: str
    date: date
    description: str


class HolidayResponse(BaseModel):
    id: int
    name: str
    date: date
    description: str

    class Config:
        from_attributes = True