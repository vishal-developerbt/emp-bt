from pydantic import BaseModel, ConfigDict
from typing import Optional


class DocumentResponse(BaseModel):
    id: str
    classification: Optional[str]
    description: Optional[str]
    document: Optional[str]
    name: Optional[str]
    process_id: Optional[str]
    profile_id: Optional[str]
    sub_process_id: Optional[str]
    tags: Optional[str]

    model_config = ConfigDict(from_attributes=True)