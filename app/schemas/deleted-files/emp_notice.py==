from pydantic import BaseModel, ConfigDict
from typing import Optional


class NoticeCreate(BaseModel):
    color: Optional[str]
    content: Optional[str]
    status: Optional[bool] = True


class NoticeUpdate(BaseModel):
    color: Optional[str]
    content: Optional[str]
    status: Optional[bool]


class NoticeResponse(BaseModel):
    id: int
    color: Optional[str]
    content: Optional[str]
    status: bool

    model_config = ConfigDict(from_attributes=True)