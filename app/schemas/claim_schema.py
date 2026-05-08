from pydantic import BaseModel, ConfigDict, Field
from datetime import date
from typing import Optional
from enum import Enum


class ClaimStatus(str, Enum):
    Pending = "Pending"
    Approved = "Approved"
    Reject = "Reject"
    ReferBack = "ReferBack"


class ClaimCreate(BaseModel):
    category: str

    mobile: Optional[str] = None

    start_date: date
    end_date: date

    amount: float = Field(gt=0)

    description: Optional[str] = None


class ClaimUpdate(BaseModel):
    category: Optional[str] = None
    mobile: Optional[str] = None

    start_date: Optional[date] = None
    end_date: Optional[date] = None

    amount: Optional[float] = None

    description: Optional[str] = None


class ClaimResponse(BaseModel):
    id: int
    user_id: int

    category: str
    mobile: Optional[str]

    start_date: date
    end_date: date

    amount: float

    status: ClaimStatus

    manager_comment: Optional[str]

    model_config = ConfigDict(from_attributes=True)


class ClaimImageCreate(BaseModel):
    claim_id: int
    file_upload: str


class ClaimImageResponse(BaseModel):
    id: int
    claim_id: int
    file_upload: str

    model_config = ConfigDict(from_attributes=True)