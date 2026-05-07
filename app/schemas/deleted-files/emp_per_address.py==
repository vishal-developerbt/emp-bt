from pydantic import BaseModel, ConfigDict
from typing import Optional


class PerAddressCreate(BaseModel):
    user_id: int
    p_house_no: str
    p_street: Optional[str]
    p_city: Optional[str]
    p_state: Optional[str]
    p_country: Optional[str]
    p_pincode: Optional[str]


class PerAddressUpdate(BaseModel):
    p_house_no: Optional[str]
    p_street: Optional[str]
    p_city: Optional[str]
    p_state: Optional[str]
    p_country: Optional[str]
    p_pincode: Optional[str]


class PerAddressResponse(BaseModel):
    id: int
    user_id: int
    p_house_no: str
    p_street: Optional[str]
    p_city: Optional[str]
    p_state: Optional[str]
    p_country: Optional[str]
    p_pincode: Optional[str]

    model_config = ConfigDict(from_attributes=True)