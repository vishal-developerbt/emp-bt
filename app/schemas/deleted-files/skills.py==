from pydantic import BaseModel, ConfigDict
from typing import Optional


class SkillCreate(BaseModel):
    skill_name: str
    user_id: int


class SkillUpdate(BaseModel):
    skill_name: Optional[str]
    user_id: Optional[int]


class SkillResponse(BaseModel):
    id: int
    skill_name: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)