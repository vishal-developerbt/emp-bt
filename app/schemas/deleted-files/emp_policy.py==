from pydantic import BaseModel, ConfigDict
from typing import Optional


class EmpPolicyCreate(BaseModel):
    hr_policy_leave_mang: Optional[str]
    hr_process_onboarding: Optional[str]
    hr_process_offboarding: Optional[str]
    status: Optional[bool] = True


class EmpPolicyUpdate(BaseModel):
    hr_policy_leave_mang: Optional[str]
    hr_process_onboarding: Optional[str]
    hr_process_offboarding: Optional[str]
    status: Optional[bool]


class EmpPolicyResponse(BaseModel):
    id: int
    hr_policy_leave_mang: Optional[str]
    hr_process_onboarding: Optional[str]
    hr_process_offboarding: Optional[str]
    status: bool

    model_config = ConfigDict(from_attributes=True)