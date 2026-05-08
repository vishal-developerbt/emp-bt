from pydantic import BaseModel, ConfigDict
from typing import Optional


class CMSCreate(BaseModel):
    title: str
    content: Optional[str] = None
    status: Optional[bool] = True


class CMSUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    status: Optional[bool] = None


class CMSResponse(BaseModel):
    id: int
    title: str
    content: Optional[str] = None
    status: bool

    model_config = ConfigDict(from_attributes=True)


class CMSImageResponse(BaseModel):
    id: int
    cms_id: int
    file_name: str
    status: bool

    model_config = ConfigDict(from_attributes=True)


class EmailTemplateCreate(BaseModel):
    subject: str
    type: str
    content: str
    status: Optional[bool] = True


class EmailTemplateUpdate(BaseModel):
    subject: Optional[str] = None
    type: Optional[str] = None
    content: Optional[str] = None
    status: Optional[bool] = None


class EmailTemplateResponse(BaseModel):
    id: int
    subject: str
    type: str
    content: str
    status: bool

    model_config = ConfigDict(from_attributes=True)


class CityStateCreate(BaseModel):
    state: str
    city: str


class CityStateUpdate(BaseModel):
    state: Optional[str] = None
    city: Optional[str] = None


class CityStateResponse(BaseModel):
    id: int
    state: str
    city: str

    model_config = ConfigDict(from_attributes=True)