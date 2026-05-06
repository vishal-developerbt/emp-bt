from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date


class IncrementCreate(BaseModel):
    user_id: int
    increment_date: Optional[date]
    increment_amount: Optional[int]
    old_salary: Optional[int]
    new_salary: Optional[int]
    comment: Optional[str]
    increment_interval: int


class IncrementUpdate(BaseModel):
    increment_date: Optional[date]
    next_increment_date: Optional[date]
    increment_amount: Optional[int]
    old_salary: Optional[int]
    new_salary: Optional[int]
    comment: Optional[str]
    is_increment_done: Optional[bool]
    increment_interval: Optional[int]


class IncrementResponse(BaseModel):
    id: int
    user_id: int
    increment_date: Optional[date]
    next_increment_date: Optional[date]
    increment_amount: Optional[int]
    old_salary: Optional[int]
    new_salary: Optional[int]
    comment: Optional[str]
    is_increment_done: bool
    increment_interval: int

    model_config = ConfigDict(from_attributes=True)