from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date


class EmpRegistrationCreate(BaseModel):
    user_id: int
    employee_code: str
    dob: date
    gender: str
    job_title: str
    employment_type: Optional[str]
    blood_group: Optional[str]

    special_leave: Optional[float] = 0
    casual_leave: Optional[float] = 0
    sick_leave: Optional[float] = 0

    employee_band: Optional[str] = "E1"
    joining_date: date
    relieving_date: Optional[date]

    accept_policy: Optional[str] = "Pending"
    status: Optional[bool] = True


class EmpRegistrationUpdate(BaseModel):
    employee_code: Optional[str]
    dob: Optional[date]
    gender: Optional[str]
    job_title: Optional[str]
    employment_type: Optional[str]
    blood_group: Optional[str]

    special_leave: Optional[float]
    casual_leave: Optional[float]
    sick_leave: Optional[float]

    employee_band: Optional[str]
    joining_date: Optional[date]
    relieving_date: Optional[date]

    accept_policy: Optional[str]
    status: Optional[bool]


class EmpRegistrationResponse(BaseModel):
    id: int
    user_id: int
    employee_code: str
    dob: date
    gender: str
    job_title: str
    employment_type: Optional[str]
    blood_group: Optional[str]

    special_leave: float
    casual_leave: float
    sick_leave: float

    employee_band: str
    joining_date: date
    relieving_date: Optional[date]

    accept_policy: str
    status: bool

    model_config = ConfigDict(from_attributes=True)