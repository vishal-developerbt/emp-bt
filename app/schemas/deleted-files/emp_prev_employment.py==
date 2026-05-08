from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional


class PrevEmploymentCreate(BaseModel):
    user_id: int
    start_date: Optional[str]
    end_date: Optional[str]
    company_name: Optional[str]
    role: Optional[str]

    company_emp_ref_name: Optional[str]
    company_emp_ref_email: Optional[EmailStr]
    company_emp_ref_mobile: Optional[str]
    company_emp_ref_role: Optional[str]


class PrevEmploymentUpdate(BaseModel):
    start_date: Optional[str]
    end_date: Optional[str]
    company_name: Optional[str]
    role: Optional[str]

    company_emp_ref_name: Optional[str]
    company_emp_ref_email: Optional[EmailStr]
    company_emp_ref_mobile: Optional[str]
    company_emp_ref_role: Optional[str]


class PrevEmploymentResponse(BaseModel):
    id: int
    user_id: int
    start_date: Optional[str]
    end_date: Optional[str]
    company_name: Optional[str]
    role: Optional[str]

    company_emp_ref_name: Optional[str]
    company_emp_ref_email: Optional[str]
    company_emp_ref_mobile: Optional[str]
    company_emp_ref_role: Optional[str]

    model_config = ConfigDict(from_attributes=True)