from pydantic import BaseModel, ConfigDict
from typing import Optional


class CityStateCreate(BaseModel):
    state: str
    city: str


class CityStateResponse(BaseModel):
    id: int
    state: str
    city: str

    model_config = ConfigDict(from_attributes=True)