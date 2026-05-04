from pydantic import BaseModel
from datetime import date


class LeaveCreate(BaseModel):
    start_date: date
    end_date: date
    reason: str


class LeaveResponse(BaseModel):
    id: int
    start_date: date
    end_date: date
    reason: str
    status: str

    class Config:
        from_attributes = True