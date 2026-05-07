from pydantic import BaseModel, ConfigDict
from typing import Optional


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