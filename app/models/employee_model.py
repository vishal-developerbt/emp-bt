from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    Time,
    TIMESTAMP,
    UniqueConstraint,
)
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.sql import func

from app.db.database import Base


# =========================================================
# ENUMS
# =========================================================

class EmployeeBand(str, PyEnum):
    E1 = "E1"
    E2 = "E2"
    E3 = "E3"
    E4 = "E4"
    E5 = "E5"


class SkillLevel(str, PyEnum):
    BEGINNER = "Beginner"
    PROFICIENT = "Proficient"
    EXPERT = "Expert"


# =========================================================
# USER
# =========================================================

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    name = Column(String(255), nullable=False)

    employee_code = Column(String(255), unique=True, nullable=False)

    role = Column(String(255), nullable=False, default="employee")

    email = Column(String(255), unique=True, nullable=False, index=True)

    email_verified_at = Column(TIMESTAMP, nullable=True)

    password = Column(String(255), nullable=False)

    remember_token = Column(String(100), nullable=True)

    reset_password_token = Column(String(100), nullable=True)

    token_status = Column(String(10), nullable=True)

    emp_shift_id = Column(
        BigInteger,
        ForeignKey("emp_shift.id"),
        default=1
    )

    technology_id = Column(
        BigInteger,
        ForeignKey("emp_technology.id"),
        nullable=True
    )

    timesheet_skip = Column(Boolean, default=False)

    is_paid = Column(Boolean, default=True)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# EMPLOYEE REGISTRATION
# =========================================================

class EmpRegistration(Base):
    __tablename__ = "emp_registrations"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(
        BigInteger,
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    employee_code = Column(String(255), nullable=False, unique=True)

    dob = Column(Date, nullable=False)

    gender = Column(String(50), nullable=False)

    job_title = Column(String(255), nullable=False)

    employment_type = Column(String(255), nullable=True)

    blood_group = Column(String(50), nullable=True)

    special_leave = Column(Float, default=0)

    casual_leave = Column(Float, default=0)

    sick_leave = Column(Float, default=0)

    employee_band = Column(
        Enum(EmployeeBand, name="employee_band_enum"),
        default=EmployeeBand.E1
    )

    joining_date = Column(Date, nullable=False)

    relieving_date = Column(Date, nullable=True)

    accept_policy = Column(String(20), default="Pending")

    status = Column(Boolean, default=True)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# ACCOUNT DETAILS
# =========================================================

class EmpAccountDetails(Base):
    __tablename__ = "emp_account_details"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(
        BigInteger,
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    bank_name = Column(String(255), nullable=True)

    acc_no = Column(String(50), nullable=True)

    ifsc = Column(String(20), nullable=True)

    salary = Column(Numeric(10, 2), default=0)

    extra_salary = Column(Integer, default=0)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# EMP ACCOUNT
# =========================================================

class EmpAccount(Base):
    __tablename__ = "emp_accounts"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(
        BigInteger,
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    profile_pic = Column(String(255), nullable=True)

    aadhar_number = Column(String(20), nullable=True)

    aadhar_doc_file = Column(String(255), nullable=True)

    pan_number = Column(String(20), nullable=True)

    pan_doc_file = Column(String(255), nullable=True)

    offer_letter = Column(String(255), nullable=True)

    relieving_letter = Column(String(255), nullable=True)

    resignation_letter = Column(String(255), nullable=True)

    appointment_letter = Column(String(255), nullable=True)

    bank_statement = Column(String(255), nullable=True)

    salary_slip1 = Column(String(255), nullable=True)

    salary_slip2 = Column(String(255), nullable=True)

    salary_slip3 = Column(String(255), nullable=True)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# ADDRESS
# =========================================================

class EmpAddress(Base):
    __tablename__ = "emp_addresses"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(
        BigInteger,
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    house_no = Column(String(255), nullable=True)

    street = Column(Text, nullable=True)

    city = Column(String(255), nullable=True)

    state = Column(String(255), nullable=True)

    country = Column(String(255), nullable=True)

    pincode = Column(String(20), nullable=True)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# EMP BAND
# =========================================================

class EmpBand(Base):
    __tablename__ = "emp_band"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    emp_band = Column(String(255), nullable=False, unique=True)

    basic_salary = Column(Float, default=0.0)

    house_rent_allowance = Column(Float, default=0.0)

    transport_allowance = Column(Float, default=0.0)

    special_allowance = Column(Float, default=0.0)

    extra_pay = Column(Float, default=0.0)

    tds_type = Column(Boolean, default=False)

    tds = Column(Float, default=0.0)

    status = Column(Boolean, default=True)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# COMMUNICATION
# =========================================================

class EmpCommunication(Base):
    __tablename__ = "emp_communications"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(
        BigInteger,
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    mobile_number = Column(String(20), nullable=True)

    company_email_id = Column(String(255), nullable=True)

    internal_email_id = Column(String(255), nullable=True)

    email_id = Column(String(255), nullable=True)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# EDUCATION
# =========================================================

class EmpEducation(Base):
    __tablename__ = "emp_education"

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    user_id = Column(
        BigInteger,
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    highschool = Column(String(255), nullable=True)

    intermediate = Column(String(255), nullable=True)

    graduation = Column(String(255), nullable=True)

    post_graduation = Column(String(255), nullable=True)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# FAMILY DETAILS
# =========================================================

class EmpFamilyDetails(Base):
    __tablename__ = "emp_family_details"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(
        BigInteger,
        ForeignKey("users.id"),
        nullable=False
    )

    father_name = Column(String(255), nullable=True)

    mother_name = Column(String(255), nullable=True)

    spouse_name = Column(String(255), nullable=True)

    number_type = Column(Integer, nullable=True)

    contact_number = Column(String(20), nullable=True)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# FEEDBACK
# =========================================================

class EmpFeedback(Base):
    __tablename__ = "emp_feedbacks"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)

    reviewer_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)

    status = Column(Boolean, default=True)

    message = Column(Text, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# INCREMENT
# =========================================================

class EmpIncrement(Base):
    __tablename__ = "emp_increment"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)

    increment_date = Column(Date, nullable=True)

    next_increment_date = Column(Date, nullable=True)

    increment_amount = Column(Float, nullable=True)

    old_salary = Column(Float, nullable=True)

    new_salary = Column(Float, nullable=True)

    comment = Column(Text, nullable=True)

    is_increment_done = Column(Boolean, default=False)

    increment_interval = Column(Integer, nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# LEAVE
# =========================================================

class EmpLeave(Base):
    __tablename__ = "emp_leaves"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)

    start_date = Column(Date, nullable=False)

    end_date = Column(Date, nullable=False)

    partial_leave = Column(String(255), nullable=True)

    leave_type = Column(String(255), nullable=False)

    project_manager = Column(String(255), nullable=False)

    approved_by = Column(BigInteger, nullable=True)

    applied_by = Column(BigInteger, nullable=False)

    cc = Column(String(255), nullable=True)

    leave_count = Column(Float, nullable=False)

    message = Column(Text, nullable=True)

    status = Column(Integer, default=0)

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# NOTICE
# =========================================================

class EmpNotice(Base):
    __tablename__ = "emp_notice"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    color = Column(String(255), nullable=True)

    content = Column(Text, nullable=True)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# PERMANENT ADDRESS
# =========================================================

class EmpPerAddress(Base):
    __tablename__ = "emp_per_address"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)

    p_house_no = Column(String(255), nullable=False)

    p_street = Column(Text, nullable=True)

    p_city = Column(String(255), nullable=True)

    p_state = Column(String(255), nullable=True)

    p_country = Column(String(255), nullable=True)

    p_pincode = Column(String(20), nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# POLICY
# =========================================================

class EmpPolicy(Base):
    __tablename__ = "emp_policy"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    hr_policy_leave_mang = Column(String(255), nullable=True)

    hr_process_onboarding = Column(String(255), nullable=True)

    hr_process_offboarding = Column(String(255), nullable=True)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# PREVIOUS EMPLOYMENT
# =========================================================

class EmpPrevEmployment(Base):
    __tablename__ = "emp_prev_employments"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)

    start_date = Column(Date, nullable=True)

    end_date = Column(Date, nullable=True)

    company_name = Column(String(255), nullable=True)

    role = Column(Text, nullable=True)

    company_emp_ref_name = Column(Text, nullable=True)

    company_emp_ref_email = Column(Text, nullable=True)

    company_emp_ref_mobile = Column(Text, nullable=True)

    company_emp_ref_role = Column(Text, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# SALARY
# =========================================================

class EmpSalary(Base):
    __tablename__ = "emp_salary"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)

    credit_salary = Column(Float, default=0)

    year = Column(Integer, nullable=False)

    month = Column(Integer, nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# SHIFT
# =========================================================

class EmpShift(Base):
    __tablename__ = "emp_shift"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    shift_name = Column(String(255), nullable=True)

    timezone = Column(String(255), nullable=True)

    shift_start_time = Column(Time, nullable=False)

    logged_in_by = Column(String(50), nullable=False)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# SHORT LEAVE
# =========================================================

class EmpShortLeave(Base):
    __tablename__ = "emp_shortleaves"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)

    start_date = Column(Date, nullable=False)

    end_date = Column(Date, nullable=False)

    partial_leave = Column(String(255), nullable=True)

    project_manager = Column(String(255), nullable=False)

    approved_by = Column(BigInteger, nullable=True)

    cc = Column(String(255), nullable=True)

    leave_count = Column(Integer, nullable=False)

    message = Column(Text, nullable=True)

    status = Column(Integer, default=0)

    comment = Column(Text, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# SKILLS
# =========================================================

class EmpSkill(Base):
    __tablename__ = "emp_skill"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    skill_id = Column(Integer, nullable=False)

    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)

    skill_level = Column(
        Enum(SkillLevel, name="skill_level_enum")
    )

    experience = Column(Float, nullable=False)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# TECHNOLOGY
# =========================================================

class EmpTechnology(Base):
    __tablename__ = "emp_technology"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    tech_name = Column(String(255), nullable=True)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# WORK FROM HOME
# =========================================================

class EmpWFH(Base):
    __tablename__ = "emp_wfhs"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)

    start_date = Column(Date, nullable=False)

    end_date = Column(Date, nullable=False)

    partial_leave = Column(String(255), nullable=True)

    project_manager = Column(String(255), nullable=False)

    approved_by = Column(BigInteger, nullable=True)

    cc = Column(String(255), nullable=True)

    leave_count = Column(Integer, nullable=False)

    message = Column(Text, nullable=True)

    status = Column(Integer, default=0)

    comment = Column(Text, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# PROFILE
# =========================================================

class Profile(Base):
    __tablename__ = "profile"

    id = Column(String(255), primary_key=True, index=True)

    created_by = Column(String(255), nullable=True)

    creation_date = Column(DateTime, default=datetime.utcnow)

    last_modified_by = Column(String(255), nullable=True)

    last_modified_date = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    email = Column(String(255), nullable=True)

    first_name = Column(String(255), nullable=True)

    last_name = Column(String(255), nullable=True)

    mobile = Column(String(255), nullable=True)

    properties = Column(JSON, nullable=True)

    type = Column(String(255), nullable=True)

    code = Column(String(255), nullable=True)

    tags = Column(String(255), nullable=True)


# =========================================================
# LOGIN SESSION
# =========================================================

class LoginSession(Base):
    __tablename__ = "login_session"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)

    status = Column(String(255), default="Login")

    work_hours = Column(Float, default=0.0)

    location = Column(String(10), default="WFO")

    comment = Column(String(255), nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )


# =========================================================
# ROLE
# =========================================================

class Role(Base):
    __tablename__ = "role"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    department = Column(String(255), nullable=False)

    access = Column(Text, nullable=True)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )