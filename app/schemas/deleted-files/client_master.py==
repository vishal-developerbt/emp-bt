from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional


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