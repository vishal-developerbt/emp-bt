from pydantic import BaseModel, ConfigDict
from typing import Optional


class CMSImageResponse(BaseModel):
    id: int
    cms_id: int
    file_name: str
    status: bool

    model_config = ConfigDict(from_attributes=True)