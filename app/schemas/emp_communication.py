from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional


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