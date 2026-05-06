from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional


# 🔹 Create
class UserCreate(BaseModel):
    name: str
    employee_code: str
    email: EmailStr
    password: str
    role: Optional[str] = "employee"
    emp_shift_id: Optional[int] = 1
    technology_id: Optional[int]


# 🔹 Update
class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]   # ✅ ADD THIS (you used it in API)
    role: Optional[str]
    emp_shift_id: Optional[int]
    technology_id: Optional[int]
    is_paid: Optional[int]
    timesheet_skip: Optional[int]


# 🔹 Login (MISSING → ADD THIS)
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# 🔹 Change Password (MISSING → ADD THIS)
class ChangePassword(BaseModel):
    old_password: str
    new_password: str


# 🔹 Response
class UserResponse(BaseModel):
    id: int
    name: str
    employee_code: str
    email: str
    role: str
    is_paid: int
    timesheet_skip: int

    model_config = ConfigDict(from_attributes=True)