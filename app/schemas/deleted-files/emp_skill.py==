from pydantic import BaseModel, ConfigDict
from typing import Optional


class EmpSkillCreate(BaseModel):
    skill_id: int
    user_id: int
    skill_level: str
    experience: float
    status: Optional[bool] = True


class EmpSkillUpdate(BaseModel):
    skill_level: Optional[str]
    experience: Optional[float]
    status: Optional[bool]


class EmpSkillResponse(BaseModel):
    id: int
    skill_id: int
    user_id: int
    skill_level: str
    experience: float
    status: bool

    model_config = ConfigDict(from_attributes=True)