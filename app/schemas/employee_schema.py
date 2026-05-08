from datetime import date, time
from decimal import Decimal
from typing import Optional, Dict, Any

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# =========================================================
# BASE CONFIG
# =========================================================

class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


# =========================================================
# EMP REGISTRATION
# =========================================================

class EmpRegistrationCreate(BaseSchema):
    user_id: int
    employee_code: str
    dob: date
    gender: str
    job_title: str

    employment_type: Optional[str] = None
    blood_group: Optional[str] = None

    special_leave: float = 0
    casual_leave: float = 0
    sick_leave: float = 0

    employee_band: str = "E1"

    joining_date: date
    relieving_date: Optional[date] = None

    accept_policy: str = "Pending"

    status: bool = True


class EmpRegistrationUpdate(BaseSchema):
    employee_code: Optional[str] = None
    dob: Optional[date] = None
    gender: Optional[str] = None
    job_title: Optional[str] = None

    employment_type: Optional[str] = None
    blood_group: Optional[str] = None

    special_leave: Optional[float] = None
    casual_leave: Optional[float] = None
    sick_leave: Optional[float] = None

    employee_band: Optional[str] = None

    joining_date: Optional[date] = None
    relieving_date: Optional[date] = None

    accept_policy: Optional[str] = None

    status: Optional[bool] = None


class EmpRegistrationResponse(EmpRegistrationCreate):
    id: int


# =========================================================
# ACCOUNT DETAILS
# =========================================================

class AccountDetailsCreate(BaseSchema):
    user_id: int

    bank_name: Optional[str] = None
    acc_no: Optional[str] = None
    ifsc: Optional[str] = None

    salary: Optional[Decimal] = 0

    extra_salary: int = 0


class AccountDetailsUpdate(BaseSchema):
    bank_name: Optional[str] = None
    acc_no: Optional[str] = None
    ifsc: Optional[str] = None

    salary: Optional[Decimal] = None

    extra_salary: Optional[int] = None


class AccountDetailsResponse(BaseSchema):
    id: int
    user_id: int

    bank_name: Optional[str]
    acc_no: Optional[str]
    ifsc: Optional[str]

    salary: Optional[Decimal]

    extra_salary: int


# =========================================================
# ACCOUNT
# =========================================================

class AccountCreate(BaseSchema):
    user_id: int

    profile_pic: Optional[str] = None

    aadhar_number: Optional[str] = None
    aadhar_doc_file: Optional[str] = None

    pan_number: Optional[str] = None
    pan_doc_file: Optional[str] = None

    offer_letter: Optional[str] = None
    relieving_letter: Optional[str] = None
    resignation_letter: Optional[str] = None
    appointment_letter: Optional[str] = None

    bank_statement: Optional[str] = None

    salary_slip1: Optional[str] = None
    salary_slip2: Optional[str] = None
    salary_slip3: Optional[str] = None


class AccountUpdate(BaseSchema):
    profile_pic: Optional[str] = None

    aadhar_number: Optional[str] = None
    aadhar_doc_file: Optional[str] = None

    pan_number: Optional[str] = None
    pan_doc_file: Optional[str] = None

    offer_letter: Optional[str] = None
    relieving_letter: Optional[str] = None
    resignation_letter: Optional[str] = None
    appointment_letter: Optional[str] = None

    bank_statement: Optional[str] = None

    salary_slip1: Optional[str] = None
    salary_slip2: Optional[str] = None
    salary_slip3: Optional[str] = None


class AccountResponse(BaseSchema):
    id: int
    user_id: int

    profile_pic: Optional[str]

    aadhar_number: Optional[str]
    pan_number: Optional[str]

    offer_letter: Optional[str]


# =========================================================
# ADDRESS
# =========================================================

class AddressCreate(BaseSchema):
    user_id: int

    house_no: Optional[str] = None
    street: Optional[str] = None

    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None

    pincode: Optional[str] = None


class AddressUpdate(BaseSchema):
    house_no: Optional[str] = None
    street: Optional[str] = None

    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None

    pincode: Optional[str] = None


class AddressResponse(AddressCreate):
    id: int


# =========================================================
# BAND
# =========================================================

class BandCreate(BaseSchema):
    emp_band: str

    basic_salary: float = 0.0

    house_rent_allowance: float = 0.0

    transport_allowance: float = 0.0

    special_allowance: float = 0.0

    extra_pay: float = 0.0

    tds_type: bool = False

    tds: float = 0.0

    status: bool = True


class BandUpdate(BaseSchema):
    emp_band: Optional[str] = None

    basic_salary: Optional[float] = None

    house_rent_allowance: Optional[float] = None

    transport_allowance: Optional[float] = None

    special_allowance: Optional[float] = None

    extra_pay: Optional[float] = None

    tds_type: Optional[bool] = None

    tds: Optional[float] = None

    status: Optional[bool] = None


class BandResponse(BandCreate):
    id: int


# =========================================================
# COMMUNICATION
# =========================================================

class CommunicationCreate(BaseSchema):
    user_id: int

    mobile_number: Optional[str] = None

    company_email_id: Optional[EmailStr] = None

    internal_email_id: Optional[EmailStr] = None

    email_id: Optional[EmailStr] = None


class CommunicationUpdate(BaseSchema):
    mobile_number: Optional[str] = None

    company_email_id: Optional[EmailStr] = None

    internal_email_id: Optional[EmailStr] = None

    email_id: Optional[EmailStr] = None


class CommunicationResponse(BaseSchema):
    id: int
    user_id: int

    mobile_number: Optional[str]

    company_email_id: Optional[EmailStr]

    internal_email_id: Optional[EmailStr]

    email_id: Optional[EmailStr]


# =========================================================
# EDUCATION
# =========================================================

class EducationCreate(BaseSchema):
    user_id: int

    highschool: Optional[str] = None
    intermediate: Optional[str] = None
    graduation: Optional[str] = None
    post_graduation: Optional[str] = None


class EducationUpdate(BaseSchema):
    highschool: Optional[str] = None
    intermediate: Optional[str] = None
    graduation: Optional[str] = None
    post_graduation: Optional[str] = None


class EducationResponse(EducationCreate):
    id: int


# =========================================================
# FAMILY
# =========================================================

class FamilyCreate(BaseSchema):
    user_id: int

    father_name: Optional[str] = None
    mother_name: Optional[str] = None
    spouse_name: Optional[str] = None

    number_type: Optional[int] = None

    contact_number: Optional[str] = None


class FamilyUpdate(BaseSchema):
    father_name: Optional[str] = None
    mother_name: Optional[str] = None
    spouse_name: Optional[str] = None

    number_type: Optional[int] = None

    contact_number: Optional[str] = None


class FamilyResponse(FamilyCreate):
    id: int


# =========================================================
# FEEDBACK
# =========================================================

class FeedbackCreate(BaseSchema):
    user_id: int
    reviewer_id: int

    message: Optional[str] = None

    status: bool = True


class FeedbackUpdate(BaseSchema):
    message: Optional[str] = None

    status: Optional[bool] = None


class FeedbackResponse(FeedbackCreate):
    id: int


# =========================================================
# INCREMENT
# =========================================================

class IncrementCreate(BaseSchema):
    user_id: int

    increment_date: Optional[date] = None
    next_increment_date: Optional[date] = None

    increment_amount: Optional[float] = None

    old_salary: Optional[float] = None
    new_salary: Optional[float] = None

    comment: Optional[str] = None

    increment_interval: int


class IncrementUpdate(BaseSchema):
    increment_date: Optional[date] = None
    next_increment_date: Optional[date] = None

    increment_amount: Optional[float] = None

    old_salary: Optional[float] = None
    new_salary: Optional[float] = None

    comment: Optional[str] = None

    is_increment_done: Optional[bool] = None

    increment_interval: Optional[int] = None


class IncrementResponse(BaseSchema):
    id: int
    user_id: int

    increment_date: Optional[date]
    next_increment_date: Optional[date]

    increment_amount: Optional[float]

    old_salary: Optional[float]
    new_salary: Optional[float]

    comment: Optional[str]

    is_increment_done: bool

    increment_interval: int


# =========================================================
# LEAVE
# =========================================================

class LeaveCreate(BaseSchema):
    user_id: int

    start_date: date
    end_date: date

    partial_leave: Optional[str] = None

    leave_type: str

    project_manager: str

    approved_by: Optional[int] = None

    applied_by: int

    cc: Optional[str] = None

    leave_count: float

    message: Optional[str] = None


class LeaveUpdate(BaseSchema):
    start_date: Optional[date] = None
    end_date: Optional[date] = None

    partial_leave: Optional[str] = None

    leave_type: Optional[str] = None

    project_manager: Optional[str] = None

    approved_by: Optional[int] = None

    cc: Optional[str] = None

    leave_count: Optional[float] = None

    message: Optional[str] = None

    status: Optional[int] = None


class LeaveResponse(LeaveCreate):
    id: int
    status: int


# =========================================================
# SHIFT
# =========================================================

class EmpShiftCreate(BaseSchema):
    shift_name: Optional[str] = None

    timezone: Optional[str] = None

    shift_start_time: time

    logged_in_by: str

    status: bool = True


class EmpShiftUpdate(BaseSchema):
    shift_name: Optional[str] = None

    timezone: Optional[str] = None

    shift_start_time: Optional[time] = None

    logged_in_by: Optional[str] = None

    status: Optional[bool] = None


class EmpShiftResponse(BaseSchema):
    id: int

    shift_name: Optional[str]

    timezone: Optional[str]

    shift_start_time: time

    logged_in_by: str

    status: bool


# =========================================================
# USER
# =========================================================

class UserCreate(BaseSchema):
    name: str

    employee_code: str

    email: EmailStr

    password: str = Field(min_length=6)

    role: str = "employee"

    emp_shift_id: int = 1

    technology_id: Optional[int] = None


class UserUpdate(BaseSchema):
    name: Optional[str] = None

    email: Optional[EmailStr] = None

    role: Optional[str] = None

    emp_shift_id: Optional[int] = None

    technology_id: Optional[int] = None

    is_paid: Optional[bool] = None

    timesheet_skip: Optional[bool] = None


class UserLogin(BaseSchema):
    email: EmailStr

    password: str


class ChangePassword(BaseSchema):
    old_password: str

    new_password: str = Field(min_length=6)


class UserResponse(BaseSchema):
    id: int

    name: str

    employee_code: str

    email: EmailStr

    role: str

    is_paid: bool

    timesheet_skip: bool


# =========================================================
# SESSION
# =========================================================

class SessionCreate(BaseSchema):
    location: str = "WFO"

    comment: Optional[str] = None


class SessionResponse(BaseSchema):
    id: int

    user_id: int

    status: str

    work_hours: float

    location: str

    comment: Optional[str]


# =========================================================
# ROLE
# =========================================================

class RoleCreate(BaseSchema):
    department: str

    access: Optional[str] = None

    status: bool = True


class RoleUpdate(BaseSchema):
    department: Optional[str] = None

    access: Optional[str] = None

    status: Optional[bool] = None


class RoleResponse(BaseSchema):
    id: int

    department: str

    access: Optional[str]

    status: bool

# =========================================================
# PROFILE
# =========================================================

class ProfileCreate(BaseSchema):
    email: Optional[EmailStr] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    mobile: Optional[str] = None

    properties: Optional[Dict[str, Any]] = None

    type: Optional[str] = None

    code: Optional[str] = None

    tags: Optional[str] = None


class ProfileUpdate(BaseSchema):
    email: Optional[EmailStr] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    mobile: Optional[str] = None

    properties: Optional[Dict[str, Any]] = None

    type: Optional[str] = None

    code: Optional[str] = None

    tags: Optional[str] = None


class ProfileResponse(BaseSchema):
    id: str

    email: Optional[EmailStr]

    first_name: Optional[str]

    last_name: Optional[str]

    mobile: Optional[str]

    properties: Optional[Dict[str, Any]]

    type: Optional[str]

    code: Optional[str]

    tags: Optional[str]

# =========================================================
# WORK FROM HOME (WFH)
# =========================================================

class EmpWFHCreate(BaseSchema):
    user_id: int

    start_date: date

    end_date: date

    partial_leave: Optional[str] = None

    project_manager: str

    approved_by: Optional[int] = None

    cc: Optional[str] = None

    leave_count: int

    message: Optional[str] = None

    status: int = 0


class EmpWFHUpdate(BaseSchema):
    start_date: Optional[date] = None

    end_date: Optional[date] = None

    partial_leave: Optional[str] = None

    project_manager: Optional[str] = None

    approved_by: Optional[int] = None

    cc: Optional[str] = None

    leave_count: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None

    comment: Optional[str] = None


class EmpWFHResponse(BaseSchema):
    id: int

    user_id: int

    start_date: date

    end_date: date

    partial_leave: Optional[str]

    project_manager: str

    approved_by: Optional[int]

    cc: Optional[str]

    leave_count: int

    message: Optional[str]

    status: int

    comment: Optional[str]

# =========================================================
# EMPLOYEE SALARY
# =========================================================

class EmpSalaryCreate(BaseSchema):
    user_id: int

    credit_salary: Optional[float] = 0

    year: int

    month: int


class EmpSalaryUpdate(BaseSchema):
    credit_salary: Optional[float] = None

    year: Optional[int] = None

    month: Optional[int] = None


class EmpSalaryResponse(BaseSchema):
    id: int

    user_id: int

    credit_salary: float

    year: int

    month: int

# =========================================================
# EMP POLICY
# =========================================================

class EmpPolicyCreate(BaseSchema):
    hr_policy_leave_mang: Optional[str] = None

    hr_process_onboarding: Optional[str] = None

    hr_process_offboarding: Optional[str] = None

    status: bool = True


class EmpPolicyUpdate(BaseSchema):
    hr_policy_leave_mang: Optional[str] = None

    hr_process_onboarding: Optional[str] = None

    hr_process_offboarding: Optional[str] = None

    status: Optional[bool] = None


class EmpPolicyResponse(BaseSchema):
    id: int

    hr_policy_leave_mang: Optional[str]

    hr_process_onboarding: Optional[str]

    hr_process_offboarding: Optional[str]

    status: bool

# =========================================================
# PREVIOUS EMPLOYMENT
# =========================================================

class PrevEmploymentCreate(BaseSchema):
    user_id: int

    start_date: Optional[date] = None

    end_date: Optional[date] = None

    company_name: Optional[str] = None

    role: Optional[str] = None

    company_emp_ref_name: Optional[str] = None

    company_emp_ref_email: Optional[EmailStr] = None

    company_emp_ref_mobile: Optional[str] = None

    company_emp_ref_role: Optional[str] = None


class PrevEmploymentUpdate(BaseSchema):
    start_date: Optional[date] = None

    end_date: Optional[date] = None

    company_name: Optional[str] = None

    role: Optional[str] = None

    company_emp_ref_name: Optional[str] = None

    company_emp_ref_email: Optional[EmailStr] = None

    company_emp_ref_mobile: Optional[str] = None

    company_emp_ref_role: Optional[str] = None


class PrevEmploymentResponse(BaseSchema):
    id: int

    user_id: int

    start_date: Optional[date]

    end_date: Optional[date]

    company_name: Optional[str]

    role: Optional[str]

    company_emp_ref_name: Optional[str]

    company_emp_ref_email: Optional[EmailStr]

    company_emp_ref_mobile: Optional[str]

    company_emp_ref_role: Optional[str]

# =========================================================
# PERMANENT ADDRESS
# =========================================================

class PerAddressCreate(BaseSchema):
    user_id: int

    p_house_no: str

    p_street: Optional[str] = None

    p_city: Optional[str] = None

    p_state: Optional[str] = None

    p_country: Optional[str] = None

    p_pincode: Optional[str] = None


class PerAddressUpdate(BaseSchema):
    p_house_no: Optional[str] = None

    p_street: Optional[str] = None

    p_city: Optional[str] = None

    p_state: Optional[str] = None

    p_country: Optional[str] = None

    p_pincode: Optional[str] = None


class PerAddressResponse(BaseSchema):
    id: int

    user_id: int

    p_house_no: str

    p_street: Optional[str]

    p_city: Optional[str]

    p_state: Optional[str]

    p_country: Optional[str]

    p_pincode: Optional[str]

# =========================================================
# NOTICE
# =========================================================

class NoticeCreate(BaseSchema):
    color: Optional[str] = None

    content: Optional[str] = None

    status: bool = True


class NoticeUpdate(BaseSchema):
    color: Optional[str] = None

    content: Optional[str] = None

    status: Optional[bool] = None


class NoticeResponse(BaseSchema):
    id: int

    color: Optional[str]

    content: Optional[str]

    status: bool

# =========================================================
# SHORT LEAVE
# =========================================================

class ShortLeaveCreate(BaseSchema):
    user_id: int

    start_date: date

    end_date: date

    partial_leave: Optional[str] = None

    project_manager: str

    approved_by: Optional[int] = None

    cc: Optional[str] = None

    leave_count: int

    message: Optional[str] = None

    status: int = 0


class ShortLeaveUpdate(BaseSchema):
    start_date: Optional[date] = None

    end_date: Optional[date] = None

    partial_leave: Optional[str] = None

    project_manager: Optional[str] = None

    approved_by: Optional[int] = None

    cc: Optional[str] = None

    leave_count: Optional[int] = None

    message: Optional[str] = None

    status: Optional[int] = None

    comment: Optional[str] = None


class ShortLeaveResponse(BaseSchema):
    id: int

    user_id: int

    start_date: date

    end_date: date

    partial_leave: Optional[str]

    project_manager: str

    approved_by: Optional[int]

    cc: Optional[str]

    leave_count: int

    message: Optional[str]

    status: int

    comment: Optional[str]

# =========================================================
# EMP TECHNOLOGY
# =========================================================

class EmpTechnologyCreate(BaseSchema):
    tech_name: Optional[str] = None

    status: bool = True


class EmpTechnologyUpdate(BaseSchema):
    tech_name: Optional[str] = None

    status: Optional[bool] = None


class EmpTechnologyResponse(BaseSchema):
    id: int

    tech_name: Optional[str]

    status: bool