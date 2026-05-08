from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional


class ClaimCreate(BaseModel):
    category: str
    mobile: Optional[str]
    start_date: date
    end_date: date
    amount: float
    description: Optional[str]


class ClaimUpdate(BaseModel):
    category: Optional[str]
    mobile: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    amount: Optional[float]
    description: Optional[str]


class ClaimResponse(BaseModel):
    id: int
    user_id: int
    category: str
    mobile: Optional[str]
    start_date: date
    end_date: date
    amount: float
    status: str
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