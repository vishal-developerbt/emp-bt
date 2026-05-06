from pydantic import BaseModel, ConfigDict
from typing import Optional


class AddressCreate(BaseModel):
    user_id: int
    house_no: Optional[str]
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    pincode: Optional[str]


class AddressUpdate(BaseModel):
    house_no: Optional[str]
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    pincode: Optional[str]


class AddressResponse(BaseModel):
    id: int
    user_id: int
    house_no: Optional[str]
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    pincode: Optional[str]

    model_config = ConfigDict(from_attributes=True)