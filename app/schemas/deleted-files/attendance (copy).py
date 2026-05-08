from pydantic import BaseModel
from datetime import datetime, date


class AttendanceResponse(BaseModel):
    id: int
    date: date
    check_in: datetime
    check_out: datetime | None

    class Config:
        from_attributes = True