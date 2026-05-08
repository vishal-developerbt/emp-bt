from pydantic import BaseModel, ConfigDict
from typing import Optional


class ManagerCreate(BaseModel):
    manager_name: str
    skill_type: Optional[str]
    status: Optional[bool] = True   # ✅ change here


class ManagerUpdate(BaseModel):
    manager_name: Optional[str]
    skill_type: Optional[str]
    status: Optional[bool]         # ✅ change here


class ManagerResponse(BaseModel):
    id: int
    manager_name: str
    skill_type: Optional[str]
    status: bool                   # ✅ change here

    model_config = ConfigDict(from_attributes=True)