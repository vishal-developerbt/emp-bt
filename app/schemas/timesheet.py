from pydantic import BaseModel, Field
from datetime import date


class TimesheetCreate(BaseModel):
    project_id: int
    date: date
    hours: int = Field(..., gt=0, le=24)
    description: str


class TimesheetResponse(BaseModel):
    id: int
    project_id: int
    date: date
    hours: int
    description: str
    status: str

    class Config:
        from_attributes = True