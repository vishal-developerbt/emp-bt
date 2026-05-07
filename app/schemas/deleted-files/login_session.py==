from pydantic import BaseModel, ConfigDict
from typing import Optional


class SessionCreate(BaseModel):
    location: Optional[str] = "WFO"
    comment: Optional[str]


class SessionResponse(BaseModel):
    id: int
    user_id: int
    status: str
    work_hours: float
    location: str
    comment: Optional[str]

    model_config = ConfigDict(from_attributes=True)