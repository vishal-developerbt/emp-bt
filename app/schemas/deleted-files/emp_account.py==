from pydantic import BaseModel, ConfigDict
from typing import Optional


class AccountCreate(BaseModel):
    user_id: int
    profile_pic: Optional[str]

    addhar_number: Optional[str]
    addhar_doc_file: Optional[str]

    pan_number: Optional[str]
    pan_doc_file: Optional[str]

    offer_letter: Optional[str]
    relieving_latter: Optional[str]
    resignation_letter: Optional[str]
    appointment_latter: Optional[str]

    bank_statment: Optional[str]

    salary_slip1: Optional[str]
    salary_slip2: Optional[str]
    salary_slip3: Optional[str]


class AccountUpdate(BaseModel):
    profile_pic: Optional[str]

    addhar_number: Optional[str]
    addhar_doc_file: Optional[str]

    pan_number: Optional[str]
    pan_doc_file: Optional[str]

    offer_letter: Optional[str]
    relieving_latter: Optional[str]
    resignation_letter: Optional[str]
    appointment_latter: Optional[str]

    bank_statment: Optional[str]

    salary_slip1: Optional[str]
    salary_slip2: Optional[str]
    salary_slip3: Optional[str]


class AccountResponse(BaseModel):
    id: int
    user_id: int
    profile_pic: Optional[str]

    addhar_number: Optional[str]
    pan_number: Optional[str]

    offer_letter: Optional[str]

    model_config = ConfigDict(from_attributes=True)