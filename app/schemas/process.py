from pydantic import BaseModel, ConfigDict
from typing import Optional, Dict, Any


class ProcessCreate(BaseModel):
    client: Optional[str]
    client_cell: Optional[str]
    client_email: Optional[str]
    client_poc: Optional[str]
    data_source: Optional[str]
    properties: Optional[Dict[str, Any]]
    rate: Optional[str]
    source: Optional[str]
    status: Optional[str]
    candidate_id: Optional[str]
    consultant: Optional[str]
    contact_id: Optional[str]
    tags: Optional[str]


class ProcessUpdate(ProcessCreate):
    pass


class ProcessResponse(ProcessCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)