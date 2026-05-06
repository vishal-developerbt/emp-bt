from pydantic import BaseModel, ConfigDict
from typing import Optional


class BandCreate(BaseModel):
    emp_band: str
    basic_salary: Optional[float] = 0.0
    house_rent_allounce: Optional[float] = 0.0
    transport_allounce: Optional[float] = 0.0
    special_allounce: Optional[float] = 0.0
    extra_pay: Optional[float] = 0.0
    tds_type: Optional[bool] = False
    tds: Optional[float] = 0.0
    status: Optional[bool] = True


class BandUpdate(BaseModel):
    emp_band: Optional[str]
    basic_salary: Optional[float]
    house_rent_allounce: Optional[float]
    transport_allounce: Optional[float]
    special_allounce: Optional[float]
    extra_pay: Optional[float]
    tds_type: Optional[bool]
    tds: Optional[float]
    status: Optional[bool]


class BandResponse(BaseModel):
    id: int
    emp_band: str
    basic_salary: float
    house_rent_allounce: float
    transport_allounce: float
    special_allounce: float
    extra_pay: float
    tds_type: bool
    tds: float
    status: bool

    model_config = ConfigDict(from_attributes=True)