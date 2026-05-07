from pydantic import BaseModel, ConfigDict
from typing import Optional


class EducationCreate(BaseModel):
    user_id: int
    highschool: Optional[str]
    intermediate: Optional[str]
    graduation: Optional[str]
    post_graduation: Optional[str]


class EducationUpdate(BaseModel):
    highschool: Optional[str]
    intermediate: Optional[str]
    graduation: Optional[str]
    post_graduation: Optional[str]


class EducationResponse(BaseModel):
    id: int
    user_id: int
    highschool: Optional[str]
    intermediate: Optional[str]
    graduation: Optional[str]
    post_graduation: Optional[str]

    model_config = ConfigDict(from_attributes=True)