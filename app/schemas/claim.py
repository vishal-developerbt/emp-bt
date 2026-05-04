from pydantic import BaseModel


class ClaimCreate(BaseModel):
    title: str
    amount: float
    description: str


class ClaimResponse(BaseModel):
    id: int
    title: str
    amount: float
    description: str
    status: str

    class Config:
        from_attributes = True