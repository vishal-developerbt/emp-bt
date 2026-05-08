from pydantic import BaseModel, ConfigDict
from typing import Optional


class EmpSalaryCreate(BaseModel):
    user_id: int
    credit_salary: Optional[str]
    year: int
    month: str


class EmpSalaryUpdate(BaseModel):
    credit_salary: Optional[str]
    year: Optional[int]
    month: Optional[str]


class EmpSalaryResponse(BaseModel):
    id: int
    user_id: int
    credit_salary: Optional[str]
    year: int
    month: str

    model_config = ConfigDict(from_attributes=True)