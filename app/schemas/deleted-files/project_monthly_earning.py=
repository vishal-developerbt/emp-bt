from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional


class EarningCreate(BaseModel):
    project_id: int
    month: date
    earning: float


class EarningUpdate(BaseModel):
    earning: Optional[float]


class EarningResponse(BaseModel):
    id: int
    project_id: int
    month: date
    earning: float

    model_config = ConfigDict(from_attributes=True)