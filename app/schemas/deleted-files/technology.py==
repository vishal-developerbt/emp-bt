from pydantic import BaseModel, ConfigDict
from typing import Optional


class TechnologyCreate(BaseModel):
    technology: Optional[str]
    status: Optional[int] = 1


class TechnologyUpdate(BaseModel):
    technology: Optional[str]
    status: Optional[int]


class TechnologyResponse(BaseModel):
    id: int
    technology: Optional[str]
    status: int

    model_config = ConfigDict(from_attributes=True)