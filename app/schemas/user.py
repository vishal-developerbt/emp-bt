from pydantic import BaseModel, EmailStr, constr
from typing import Literal, Optional
from datetime import date, datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=6, max_length=72)
    role: Literal["admin", "employee"] = "employee"  

class UserLogin(BaseModel):
    identifier: str
    password: str

class ChangePassword(BaseModel):
    old_password: str
    new_password: constr(min_length=6, max_length=72)


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class VerifyOTP(BaseModel):
    email: EmailStr
    otp: str


class ResetPassword(BaseModel):
    email: EmailStr
    otp: str
    new_password: constr(min_length=6, max_length=72)

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    username: str
    role: str

    class Config:
        from_attributes = True
        
class UserUpdate(BaseModel):
    name: str
    email: str
    role: str        
# 👤 Profile Response Schema
class UserProfile(BaseModel):
    id: int
    name: str
    email: EmailStr
    username: str

    dob: Optional[date] = None
    gender: Optional[str] = None
    blood_group: Optional[str] = None
    joining_date: Optional[date] = None
    employee_type: Optional[str] = None
    employee_band: Optional[str] = None
    job_title: Optional[str] = None
    shift: Optional[str] = None

    class Config:
        from_attributes = True


# ✏️ Update Profile Schema
class UpdateProfile(BaseModel):
    name: Optional[str] = None
    dob: Optional[date] = None
    gender: Optional[str] = None
    blood_group: Optional[str] = None
    joining_date: Optional[date] = None
    employee_type: Optional[str] = None
    employee_band: Optional[str] = None
    job_title: Optional[str] = None
    shift: Optional[str] = None