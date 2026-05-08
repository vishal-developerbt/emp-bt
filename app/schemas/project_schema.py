from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import date
from typing import Optional, Dict, Any


# =========================
# PROJECT
# =========================
class ProjectCreate(BaseModel):
    project_name: str
    vendor_name: str
    project_startdate: date
    project_enddate: Optional[date] = None
    status: Optional[bool] = True
    is_billable: Optional[int] = 1


class ProjectUpdate(BaseModel):
    project_name: Optional[str] = None
    vendor_name: Optional[str] = None
    project_startdate: Optional[date] = None
    project_enddate: Optional[date] = None
    status: Optional[bool] = None
    is_billable: Optional[int] = None


class ProjectResponse(BaseModel):
    id: int
    project_name: str
    vendor_name: str
    project_startdate: date
    project_enddate: Optional[date]
    status: bool
    is_billable: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# PROJECT MANAGER
# =========================
class ProjectManagerCreate(BaseModel):
    project_id: int
    manager_id: int
    developer_id: int
    technology_id: int
    status: Optional[bool] = True
    resource_type: Optional[bool] = False


class ProjectManagerUpdate(BaseModel):
    project_id: Optional[int] = None
    manager_id: Optional[int] = None
    developer_id: Optional[int] = None
    technology_id: Optional[int] = None
    status: Optional[bool] = None
    resource_type: Optional[bool] = None


class ProjectManagerResponse(BaseModel):
    id: int
    project_id: int
    manager_id: int
    developer_id: int
    technology_id: int
    status: bool
    resource_type: bool

    model_config = ConfigDict(from_attributes=True)


# =========================
# EARNING
# =========================
class EarningCreate(BaseModel):
    project_id: int
    month: date
    earning: float


class EarningUpdate(BaseModel):
    earning: Optional[float] = None


class EarningResponse(BaseModel):
    id: int
    project_id: int
    month: date
    earning: float

    model_config = ConfigDict(from_attributes=True)


# =========================
# TECHNOLOGY
# =========================
class TechnologyCreate(BaseModel):
    technology: Optional[str] = None
    status: Optional[bool] = True


class TechnologyUpdate(BaseModel):
    technology: Optional[str] = None
    status: Optional[bool] = None


class TechnologyResponse(BaseModel):
    id: int
    technology: Optional[str]
    status: bool

    model_config = ConfigDict(from_attributes=True)


# =========================
# SKILL
# =========================
class SkillCreate(BaseModel):
    skill_name: str
    user_id: int


class SkillUpdate(BaseModel):
    skill_name: Optional[str] = None
    user_id: Optional[int] = None


class SkillResponse(BaseModel):
    id: int
    skill_name: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# SKILL DEPARTMENT
# =========================
class SkillDepartmentCreate(BaseModel):
    skill_name: str
    status: Optional[bool] = True   # FIXED (was str)


class SkillDepartmentUpdate(BaseModel):
    skill_name: Optional[str] = None
    status: Optional[bool] = None


class SkillDepartmentResponse(BaseModel):
    id: int
    skill_name: str
    status: bool

    model_config = ConfigDict(from_attributes=True)


# =========================
# TEAM LEAD
# =========================
class TeamLeadCreate(BaseModel):
    manager_id: Optional[int] = None
    teamlead_id: Optional[int] = None
    user_id: Optional[int] = None
    status: Optional[bool] = False   # FIXED (was int)


class TeamLeadUpdate(BaseModel):
    manager_id: Optional[int] = None
    teamlead_id: Optional[int] = None
    user_id: Optional[int] = None
    status: Optional[bool] = None


class TeamLeadResponse(BaseModel):
    id: int
    manager_id: Optional[int]
    teamlead_id: Optional[int]
    user_id: Optional[int]
    status: bool

    model_config = ConfigDict(from_attributes=True)


# =========================
# MANAGER
# =========================
class ManagerCreate(BaseModel):
    manager_name: str
    skill_type: Optional[str] = None
    status: Optional[bool] = True


class ManagerUpdate(BaseModel):
    manager_name: Optional[str] = None
    skill_type: Optional[str] = None
    status: Optional[bool] = None


class ManagerResponse(BaseModel):
    id: int
    manager_name: str
    skill_type: Optional[str]
    status: bool

    model_config = ConfigDict(from_attributes=True)


# =========================
# CLIENT
# =========================
class ClientCreate(BaseModel):
    technology: Optional[str] = None
    interview_date: Optional[str] = None
    company: Optional[str] = None
    name: Optional[str] = None
    contact_person: Optional[str] = None
    client_email: Optional[EmailStr] = None
    contact_number: Optional[str] = None
    source: Optional[str] = None
    rate: Optional[str] = None
    pre_call_notes: Optional[str] = None
    meeting_link: Optional[str] = None
    post_call_notes: Optional[str] = None
    status: Optional[str] = None
    interview_taken_by: Optional[str] = None
    end_client: Optional[str] = None
    interview_type: Optional[str] = None


class ClientUpdate(ClientCreate):
    pass


class ClientResponse(ClientCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


# =========================
# PROCESS
# =========================
class ProcessCreate(BaseModel):
    client: Optional[str] = None
    client_cell: Optional[str] = None
    client_email: Optional[str] = None
    client_poc: Optional[str] = None
    data_source: Optional[str] = None
    properties: Optional[Dict[str, Any]] = None
    rate: Optional[str] = None
    source: Optional[str] = None
    status: Optional[str] = None
    candidate_id: Optional[str] = None
    consultant: Optional[str] = None
    contact_id: Optional[str] = None
    tags: Optional[str] = None


class ProcessUpdate(ProcessCreate):
    pass


class ProcessResponse(ProcessCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)


# =========================
# SUB PROCESS
# =========================
class SubProcessCreate(BaseModel):
    client_cell: Optional[str] = None
    client_email: Optional[str] = None
    interview_date: str
    interview_mode: Optional[str] = None
    interview_panel: Optional[str] = None
    meeting_invite: Optional[str] = None
    note: Optional[str] = None
    properties: Optional[Dict[str, Any]] = None
    status: Optional[str] = None
    time: Optional[str] = None
    consultant_id: Optional[str] = None
    process_id: Optional[str] = None
    profile: Optional[str] = None


class SubProcessUpdate(SubProcessCreate):
    pass


class SubProcessResponse(SubProcessCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)


# =========================
# DEPARTMENT
# =========================
class DepartmentCreate(BaseModel):
    department_name: str
    status: Optional[bool] = True


class DepartmentUpdate(BaseModel):
    department_name: Optional[str] = None
    status: Optional[bool] = None


class DepartmentResponse(BaseModel):
    id: int
    department_name: str
    status: bool

    model_config = ConfigDict(from_attributes=True)


# =========================
# DOCUMENT
# =========================
class DocumentResponse(BaseModel):
    id: str
    classification: Optional[str]
    description: Optional[str]
    document: Optional[str]
    name: Optional[str]
    process_id: Optional[str]
    profile_id: Optional[str]
    sub_process_id: Optional[str]
    tags: Optional[str]

    model_config = ConfigDict(from_attributes=True)