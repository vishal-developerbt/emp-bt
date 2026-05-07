from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional, Dict, Any
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



class AccountCreate(BaseModel):
    user_id: int
    profile_pic: Optional[str]

    addhar_number: Optional[str]
    addhar_doc_file: Optional[str]

    pan_number: Optional[str]
    pan_doc_file: Optional[str]

    offer_letter: Optional[str]
    relieving_latter: Optional[str]
    resignation_letter: Optional[str]
    appointment_latter: Optional[str]

    bank_statment: Optional[str]

    salary_slip1: Optional[str]
    salary_slip2: Optional[str]
    salary_slip3: Optional[str]


class AccountUpdate(BaseModel):
    profile_pic: Optional[str]

    addhar_number: Optional[str]
    addhar_doc_file: Optional[str]

    pan_number: Optional[str]
    pan_doc_file: Optional[str]

    offer_letter: Optional[str]
    relieving_latter: Optional[str]
    resignation_letter: Optional[str]
    appointment_latter: Optional[str]

    bank_statment: Optional[str]

    salary_slip1: Optional[str]
    salary_slip2: Optional[str]
    salary_slip3: Optional[str]


class AccountResponse(BaseModel):
    id: int
    user_id: int
    profile_pic: Optional[str]

    addhar_number: Optional[str]
    pan_number: Optional[str]

    offer_letter: Optional[str]

    model_config = ConfigDict(from_attributes=True)


class AddressCreate(BaseModel):
    user_id: int
    house_no: Optional[str]
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    pincode: Optional[str]


class AddressUpdate(BaseModel):
    house_no: Optional[str]
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    pincode: Optional[str]


class AddressResponse(BaseModel):
    id: int
    user_id: int
    house_no: Optional[str]
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    pincode: Optional[str]

    model_config = ConfigDict(from_attributes=True)



class BandCreate(BaseModel):
    emp_band: str
    basic_salary: Optional[float] = 0.0
    house_rent_allounce: Optional[float] = 0.0
    transport_allounce: Optional[float] = 0.0
    special_allounce: Optional[float] = 0.0
    extra_pay: Optional[float] = 0.0
    tds_type: Optional[bool] = False
    tds: Optional[float] = 0.0
    status: Optional[bool] = True


class BandUpdate(BaseModel):
    emp_band: Optional[str]
    basic_salary: Optional[float]
    house_rent_allounce: Optional[float]
    transport_allounce: Optional[float]
    special_allounce: Optional[float]
    extra_pay: Optional[float]
    tds_type: Optional[bool]
    tds: Optional[float]
    status: Optional[bool]


class BandResponse(BaseModel):
    id: int
    emp_band: str
    basic_salary: float
    house_rent_allounce: float
    transport_allounce: float
    special_allounce: float
    extra_pay: float
    tds_type: bool
    tds: float
    status: bool

    model_config = ConfigDict(from_attributes=True)

class CommunicationCreate(BaseModel):
    user_id: int
    mobile_number: Optional[str]
    company_email_id: Optional[EmailStr]
    internal_email_id: Optional[EmailStr]
    email_id: Optional[EmailStr]


class CommunicationUpdate(BaseModel):
    mobile_number: Optional[str]
    company_email_id: Optional[EmailStr]
    internal_email_id: Optional[EmailStr]
    email_id: Optional[EmailStr]


class CommunicationResponse(BaseModel):
    id: int
    user_id: int
    mobile_number: Optional[str]
    company_email_id: Optional[str]
    internal_email_id: Optional[str]
    email_id: Optional[str]

    model_config = ConfigDict(from_attributes=True)


class EducationCreate(BaseModel):
    user_id: int
    highschool: Optional[str]
    intermediate: Optional[str]
    graduation: Optional[str]
    post_graduation: Optional[str]


class EducationUpdate(BaseModel):
    highschool: Optional[str]
    intermediate: Optional[str]
    graduation: Optional[str]
    post_graduation: Optional[str]


class EducationResponse(BaseModel):
    id: int
    user_id: int
    highschool: Optional[str]
    intermediate: Optional[str]
    graduation: Optional[str]
    post_graduation: Optional[str]

    model_config = ConfigDict(from_attributes=True)


class FamilyCreate(BaseModel):
    user_id: int
    father_name: Optional[str]
    mother_name: Optional[str]
    spouse_name: Optional[str]
    number_type: Optional[int]
    contact_number: Optional[str]


class FamilyUpdate(BaseModel):
    father_name: Optional[str]
    mother_name: Optional[str]
    spouse_name: Optional[str]
    number_type: Optional[int]
    contact_number: Optional[str]


class FamilyResponse(BaseModel):
    id: int
    user_id: int
    father_name: Optional[str]
    mother_name: Optional[str]
    spouse_name: Optional[str]
    number_type: Optional[int]
    contact_number: Optional[str]

    model_config = ConfigDict(from_attributes=True)

class FeedbackCreate(BaseModel):
    user_id: int
    reviewer_id: int
    message: Optional[str]
    status: Optional[bool] = True


class FeedbackUpdate(BaseModel):
    message: Optional[str]
    status: Optional[bool]


class FeedbackResponse(BaseModel):
    id: int
    user_id: int
    reviewer_id: int
    message: Optional[str]
    status: bool

    model_config = ConfigDict(from_attributes=True)



class IncrementCreate(BaseModel):
    user_id: int
    increment_date: Optional[date]
    increment_amount: Optional[int]
    old_salary: Optional[int]
    new_salary: Optional[int]
    comment: Optional[str]
    increment_interval: int


class IncrementUpdate(BaseModel):
    increment_date: Optional[date]
    next_increment_date: Optional[date]
    increment_amount: Optional[int]
    old_salary: Optional[int]
    new_salary: Optional[int]
    comment: Optional[str]
    is_increment_done: Optional[bool]
    increment_interval: Optional[int]


class IncrementResponse(BaseModel):
    id: int
    user_id: int
    increment_date: Optional[date]
    next_increment_date: Optional[date]
    increment_amount: Optional[int]
    old_salary: Optional[int]
    new_salary: Optional[int]
    comment: Optional[str]
    is_increment_done: bool
    increment_interval: int

    model_config = ConfigDict(from_attributes=True)


class LeaveCreate(BaseModel):
    user_id: int
    start_date: date
    end_date: date
    partical_leave: Optional[str]
    leave_type: str
    project_manager: str
    approved_by: Optional[int]
    applied_by: int
    cc: Optional[str]
    leave_count: float
    message: Optional[str]


class LeaveUpdate(BaseModel):
    start_date: Optional[date]
    end_date: Optional[date]
    partical_leave: Optional[str]
    leave_type: Optional[str]
    project_manager: Optional[str]
    approved_by: Optional[int]
    cc: Optional[str]
    leave_count: Optional[float]
    message: Optional[str]
    status: Optional[int]


class LeaveResponse(BaseModel):
    id: int
    user_id: int
    start_date: date
    end_date: date
    partical_leave: Optional[str]
    leave_type: str
    project_manager: str
    approved_by: Optional[int]
    applied_by: int
    cc: Optional[str]
    leave_count: float
    message: Optional[str]
    status: int

    model_config = ConfigDict(from_attributes=True)

class NoticeCreate(BaseModel):
    color: Optional[str]
    content: Optional[str]
    status: Optional[bool] = True


class NoticeUpdate(BaseModel):
    color: Optional[str]
    content: Optional[str]
    status: Optional[bool]


class NoticeResponse(BaseModel):
    id: int
    color: Optional[str]
    content: Optional[str]
    status: bool

    model_config = ConfigDict(from_attributes=True)



class PerAddressCreate(BaseModel):
    user_id: int
    p_house_no: str
    p_street: Optional[str]
    p_city: Optional[str]
    p_state: Optional[str]
    p_country: Optional[str]
    p_pincode: Optional[str]


class PerAddressUpdate(BaseModel):
    p_house_no: Optional[str]
    p_street: Optional[str]
    p_city: Optional[str]
    p_state: Optional[str]
    p_country: Optional[str]
    p_pincode: Optional[str]


class PerAddressResponse(BaseModel):
    id: int
    user_id: int
    p_house_no: str
    p_street: Optional[str]
    p_city: Optional[str]
    p_state: Optional[str]
    p_country: Optional[str]
    p_pincode: Optional[str]

    model_config = ConfigDict(from_attributes=True)


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

class EmpShiftCreate(BaseModel):
    shift_name: Optional[str]
    timezone: Optional[str]
    shift_start_time: str
    logged_in_by: str
    status: Optional[str] = "Enable"


class EmpShiftUpdate(BaseModel):
    shift_name: Optional[str]
    timezone: Optional[str]
    shift_start_time: Optional[str]
    logged_in_by: Optional[str]
    status: Optional[str]


class EmpShiftResponse(BaseModel):
    id: int
    shift_name: Optional[str]
    timezone: Optional[str]
    shift_start_time: str
    logged_in_by: str
    status: str

    model_config = ConfigDict(from_attributes=True)



class ShortLeaveCreate(BaseModel):
    user_id: int
    start_date: date
    end_date: date
    partical_leave: Optional[str]
    project_manager: str
    approved_by: Optional[int]
    cc: Optional[str]
    leave_count: int
    message: Optional[str]
    status: Optional[int] = 0


class ShortLeaveUpdate(BaseModel):
    start_date: Optional[date]
    end_date: Optional[date]
    partical_leave: Optional[str]
    project_manager: Optional[str]
    approved_by: Optional[int]
    cc: Optional[str]
    leave_count: Optional[int]
    message: Optional[str]
    status: Optional[int]
    comment: Optional[str]


class ShortLeaveResponse(BaseModel):
    id: int
    user_id: int
    start_date: date
    end_date: date
    partical_leave: Optional[str]
    project_manager: str
    approved_by: Optional[int]
    cc: Optional[str]
    leave_count: int
    message: Optional[str]
    status: int
    comment: Optional[str]

    model_config = ConfigDict(from_attributes=True)

class EmpSkillCreate(BaseModel):
    skill_id: int
    user_id: int
    skill_level: str
    experience: float
    status: Optional[bool] = True


class EmpSkillUpdate(BaseModel):
    skill_level: Optional[str]
    experience: Optional[float]
    status: Optional[bool]


class EmpSkillResponse(BaseModel):
    id: int
    skill_id: int
    user_id: int
    skill_level: str
    experience: float
    status: bool

    model_config = ConfigDict(from_attributes=True)

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


class EmpWFHCreate(BaseModel):
    user_id: int
    start_date: date
    end_date: date
    partical_leave: Optional[str]
    project_manager: str
    approved_by: Optional[int]
    cc: Optional[str]
    leave_count: int
    message: Optional[str]
    status: Optional[int] = 0


class EmpWFHUpdate(BaseModel):
    start_date: Optional[date]
    end_date: Optional[date]
    partical_leave: Optional[str]
    project_manager: Optional[str]
    approved_by: Optional[int]
    cc: Optional[str]
    leave_count: Optional[int]
    message: Optional[str]
    status: Optional[int]
    comment: Optional[str]


class EmpWFHResponse(BaseModel):
    id: int
    user_id: int
    start_date: date
    end_date: date
    partical_leave: Optional[str]
    project_manager: str
    approved_by: Optional[int]
    cc: Optional[str]
    leave_count: int
    message: Optional[str]
    status: int
    comment: Optional[str]

    model_config = ConfigDict(from_attributes=True)


class ProfileCreate(BaseModel):
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    mobile: Optional[str]
    properties: Optional[Dict[str, Any]]
    type: Optional[str]
    code: Optional[str]
    tags: Optional[str]


class ProfileUpdate(ProfileCreate):
    pass


class ProfileResponse(ProfileCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)


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

class SessionCreate(BaseModel):
    location: Optional[str] = "WFO"
    comment: Optional[str]


class SessionResponse(BaseModel):
    id: int
    user_id: int
    status: str
    work_hours: float
    location: str
    comment: Optional[str]

    model_config = ConfigDict(from_attributes=True)

class RoleCreate(BaseModel):
    department: str
    access: Optional[str] = None
    status: Optional[bool] = True


class RoleUpdate(BaseModel):
    department: Optional[str]
    access: Optional[str]
    status: Optional[bool]


class RoleResponse(BaseModel):
    id: int
    department: str
    access: Optional[str]
    status: bool

    class Config:
        from_attributes = True