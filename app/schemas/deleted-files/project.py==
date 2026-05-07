from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional


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