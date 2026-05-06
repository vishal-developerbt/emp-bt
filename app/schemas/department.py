from pydantic import BaseModel, ConfigDict
from typing import Optional


class DepartmentCreate(BaseModel):
    department_name: str
    status: Optional[bool] = True


class DepartmentUpdate(BaseModel):
    department_name: Optional[str]
    status: Optional[bool]


class DepartmentResponse(BaseModel):
    id: int
    department_name: str
    status: bool

    model_config = ConfigDict(from_attributes=True)