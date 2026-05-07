from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import date
from typing import Optional, Dict, Any


class ProjectCreate(BaseModel):
    project_name: str
    vendor_name: str
    project_startdate: date
    project_enddate: Optional[date]
    status: Optional[bool] = True
    is_billable: Optional[int] = 1


class ProjectUpdate(BaseModel):
    project_name: Optional[str]
    vendor_name: Optional[str]
    project_startdate: Optional[date]
    project_enddate: Optional[date]
    status: Optional[bool]
    is_billable: Optional[int]


class ProjectResponse(BaseModel):
    id: int
    project_name: str
    vendor_name: str
    project_startdate: date
    project_enddate: Optional[date]
    status: bool
    is_billable: int

    model_config = ConfigDict(from_attributes=True)


class ProjectManagerCreate(BaseModel):
    project_id: int
    manager_id: int
    developer_id: int
    technology_id: int
    status: Optional[bool] = True
    resource_type: Optional[bool] = False


class ProjectManagerUpdate(BaseModel):
    project_id: Optional[int]
    manager_id: Optional[int]
    developer_id: Optional[int]
    technology_id: Optional[int]
    status: Optional[bool]
    resource_type: Optional[bool]


class ProjectManagerResponse(BaseModel):
    id: int
    project_id: int
    manager_id: int
    developer_id: int
    technology_id: int
    status: bool
    resource_type: bool

    model_config = ConfigDict(from_attributes=True)

class EarningCreate(BaseModel):
    project_id: int
    month: date
    earning: float


class EarningUpdate(BaseModel):
    earning: Optional[float]


class EarningResponse(BaseModel):
    id: int
    project_id: int
    month: date
    earning: float

    model_config = ConfigDict(from_attributes=True)

class TechnologyCreate(BaseModel):
    technology: Optional[str]
    status: Optional[int] = 1


class TechnologyUpdate(BaseModel):
    technology: Optional[str]
    status: Optional[int]


class TechnologyResponse(BaseModel):
    id: int
    technology: Optional[str]
    status: int

    model_config = ConfigDict(from_attributes=True)

class SkillCreate(BaseModel):
    skill_name: str
    user_id: int


class SkillUpdate(BaseModel):
    skill_name: Optional[str]
    user_id: Optional[int]


class SkillResponse(BaseModel):
    id: int
    skill_name: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)

class SkillDepartmentCreate(BaseModel):
    skill_name: str
    status: Optional[str] = "1"


class SkillDepartmentUpdate(BaseModel):
    skill_name: Optional[str]
    status: Optional[str]


class SkillDepartmentResponse(BaseModel):
    id: int
    skill_name: str
    status: str

    model_config = ConfigDict(from_attributes=True)


class TeamLeadCreate(BaseModel):
    manager_id: Optional[int]
    teamlead_id: Optional[int]
    user_id: Optional[int]
    status: Optional[int] = 1


class TeamLeadUpdate(BaseModel):
    manager_id: Optional[int]
    teamlead_id: Optional[int]
    user_id: Optional[int]
    status: Optional[int]


class TeamLeadResponse(BaseModel):
    id: int
    manager_id: Optional[int]
    teamlead_id: Optional[int]
    user_id: Optional[int]
    status: int

    model_config = ConfigDict(from_attributes=True)

class ManagerCreate(BaseModel):
    manager_name: str
    skill_type: Optional[str]
    status: Optional[bool] = True   # ✅ change here


class ManagerUpdate(BaseModel):
    manager_name: Optional[str]
    skill_type: Optional[str]
    status: Optional[bool]         # ✅ change here


class ManagerResponse(BaseModel):
    id: int
    manager_name: str
    skill_type: Optional[str]
    status: bool                   # ✅ change here

    model_config = ConfigDict(from_attributes=True)

class ClientCreate(BaseModel):
    technology: Optional[str]
    interview_date: Optional[str]
    company: Optional[str]
    name: Optional[str]
    contact_person: Optional[str]
    client_email: Optional[EmailStr]
    contact_number: Optional[str]
    source: Optional[str]
    rate: Optional[str]
    pre_call_notes: Optional[str]
    meeting_link: Optional[str]
    post_call_notes: Optional[str]
    status: Optional[str]
    interview_taken_by: Optional[str]
    end_client: Optional[str]
    interview_type: Optional[str]


class ClientUpdate(ClientCreate):
    pass


class ClientResponse(ClientCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ProcessCreate(BaseModel):
    client: Optional[str]
    client_cell: Optional[str]
    client_email: Optional[str]
    client_poc: Optional[str]
    data_source: Optional[str]
    properties: Optional[Dict[str, Any]]
    rate: Optional[str]
    source: Optional[str]
    status: Optional[str]
    candidate_id: Optional[str]
    consultant: Optional[str]
    contact_id: Optional[str]
    tags: Optional[str]


class ProcessUpdate(ProcessCreate):
    pass


class ProcessResponse(ProcessCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)


class SubProcessCreate(BaseModel):
    client_cell: Optional[str]
    client_email: Optional[str]
    interview_date: str
    interview_mode: Optional[str]
    interview_panel: Optional[str]
    meeting_invite: Optional[str]
    note: Optional[str]
    properties: Optional[Dict[str, Any]]
    status: Optional[str]
    time: Optional[str]
    consultant_id: Optional[str]
    process_id: Optional[str]
    profile: Optional[str]


class SubProcessUpdate(SubProcessCreate):
    pass


class SubProcessResponse(SubProcessCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)

class DepartmentCreate(BaseModel):
    department_name: str
    status: Optional[bool] = True


class DepartmentUpdate(BaseModel):
    department_name: Optional[str]
    status: Optional[bool]


class DepartmentResponse(BaseModel):
    id: int
    department_name: str
    status: bool

    model_config = ConfigDict(from_attributes=True)


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