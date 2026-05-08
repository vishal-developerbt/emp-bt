from pydantic import BaseModel, ConfigDict
from typing import Optional


class EmpTechnologyCreate(BaseModel):
    tech_name: Optional[str]
    status: Optional[bool] = True


class EmpTechnologyUpdate(BaseModel):
    tech_name: Optional[str]
    status: Optional[bool]


class EmpTechnologyResponse(BaseModel):
    id: int
    tech_name: Optional[str]
    status: bool

    model_config = ConfigDict(from_attributes=True)