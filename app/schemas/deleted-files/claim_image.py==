from pydantic import BaseModel, ConfigDict
from typing import Optional


class ClaimImageCreate(BaseModel):
    claim_id: int
    file_upload: str


class ClaimImageResponse(BaseModel):
    id: int
    claim_id: int
    file_upload: str

    model_config = ConfigDict(from_attributes=True)