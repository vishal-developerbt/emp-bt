from pydantic import BaseModel, ConfigDict
from typing import Optional


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