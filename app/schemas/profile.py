from pydantic import BaseModel, ConfigDict
from typing import Optional, Dict, Any


class ProfileCreate(BaseModel):
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    mobile: Optional[str]
    properties: Optional[Dict[str, Any]]
    type: Optional[str]
    code: Optional[str]
    tags: Optional[str]


class ProfileUpdate(ProfileCreate):
    pass


class ProfileResponse(ProfileCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)