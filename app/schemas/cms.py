from pydantic import BaseModel, ConfigDict
from typing import Optional


class CMSCreate(BaseModel):
    title: str
    content: Optional[str]
    status: Optional[bool] = True


class CMSUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    status: Optional[bool]


class CMSResponse(BaseModel):
    id: int
    title: str
    content: Optional[str]
    status: bool

    model_config = ConfigDict(from_attributes=True)