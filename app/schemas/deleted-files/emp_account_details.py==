from pydantic import BaseModel, ConfigDict
from typing import Optional


class AccountDetailsCreate(BaseModel):
    user_id: int
    bank_name: Optional[str]
    acc_no: Optional[str]
    ifsc: Optional[str]
    salary: Optional[str]
    extra_salary: Optional[int] = 0


class AccountDetailsUpdate(BaseModel):
    bank_name: Optional[str]
    acc_no: Optional[str]
    ifsc: Optional[str]
    salary: Optional[str]
    extra_salary: Optional[int]


class AccountDetailsResponse(BaseModel):
    id: int
    user_id: int
    bank_name: Optional[str]
    ifsc: Optional[str]
    salary: Optional[str]
    extra_salary: Optional[int]

    model_config = ConfigDict(from_attributes=True)