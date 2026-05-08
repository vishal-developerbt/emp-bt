from pydantic import BaseModel, ConfigDict
from typing import Optional


class EmailTemplateCreate(BaseModel):
    subject: str
    type: str
    content: str
    status: Optional[bool] = True


class EmailTemplateUpdate(BaseModel):
    subject: Optional[str]
    type: Optional[str]
    content: Optional[str]
    status: Optional[bool]


class EmailTemplateResponse(BaseModel):
    id: int
    subject: str
    type: str
    content: str
    status: bool

    model_config = ConfigDict(from_attributes=True)