from pydantic import BaseModel, ConfigDict
from typing import Optional, Dict, Any


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