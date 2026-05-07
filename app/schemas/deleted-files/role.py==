from pydantic import BaseModel
from typing import Optional


class RoleCreate(BaseModel):
    department: str
    access: Optional[str] = None
    status: Optional[bool] = True


class RoleUpdate(BaseModel):
    department: Optional[str]
    access: Optional[str]
    status: Optional[bool]


class RoleResponse(BaseModel):
    id: int
    department: str
    access: Optional[str]
    status: bool

    class Config:
        from_attributes = True