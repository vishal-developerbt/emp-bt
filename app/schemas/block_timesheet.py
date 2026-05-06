from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional


class BlockCreate(BaseModel):
    timesheet_date: date
    user_id: Optional[int] = 0
    is_block: Optional[bool] = True


class BlockUpdate(BaseModel):
    is_block: Optional[bool]


class BlockResponse(BaseModel):
    id: int
    timesheet_date: date
    is_block: bool
    user_id: int
    approved_by: Optional[int]

    model_config = ConfigDict(from_attributes=True)