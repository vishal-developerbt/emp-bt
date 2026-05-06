from pydantic import BaseModel, ConfigDict
from typing import Optional


class SkillDepartmentCreate(BaseModel):
    skill_name: str
    status: Optional[str] = "1"


class SkillDepartmentUpdate(BaseModel):
    skill_name: Optional[str]
    status: Optional[str]


class SkillDepartmentResponse(BaseModel):
    id: int
    skill_name: str
    status: str

    model_config = ConfigDict(from_attributes=True)