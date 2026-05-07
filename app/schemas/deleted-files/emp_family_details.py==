from pydantic import BaseModel, ConfigDict
from typing import Optional


class FamilyCreate(BaseModel):
    user_id: int
    father_name: Optional[str]
    mother_name: Optional[str]
    spouse_name: Optional[str]
    number_type: Optional[int]
    contact_number: Optional[str]


class FamilyUpdate(BaseModel):
    father_name: Optional[str]
    mother_name: Optional[str]
    spouse_name: Optional[str]
    number_type: Optional[int]
    contact_number: Optional[str]


class FamilyResponse(BaseModel):
    id: int
    user_id: int
    father_name: Optional[str]
    mother_name: Optional[str]
    spouse_name: Optional[str]
    number_type: Optional[int]
    contact_number: Optional[str]

    model_config = ConfigDict(from_attributes=True)