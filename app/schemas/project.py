from pydantic import BaseModel
from datetime import date

class ProjectCreate(BaseModel):
    name: str
    description: str


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True

# New schema for assigning project
class AssignProjectRequest(BaseModel):
    username: str
    project_id: int
    project_manager_user_id: int
    project_start_date: date

