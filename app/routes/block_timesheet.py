from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.core.deps import get_current_user
from app.models.attendance_model import BlockTimesheet

from datetime import date
from app.schemas.attendance_schema import (
    BlockCreate,
    BlockUpdate,
    BlockResponse
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BlockResponse)
def create_block(
    data: BlockCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    existing = db.query(BlockTimesheet).filter(
        BlockTimesheet.timesheet_date == data.timesheet_date,
        BlockTimesheet.user_id == data.user_id
    ).first()

    if existing:
        raise HTTPException(400, "Block already exists")

    block = BlockTimesheet(
        **data.dict(),
        approved_by=current_user.id
    )

    db.add(block)
    db.commit()
    db.refresh(block)

    return block

@router.put("/{id}", response_model=BlockResponse)
def update_block(
    id: int,
    data: BlockUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    block = db.query(BlockTimesheet).filter(BlockTimesheet.id == id).first()

    if not block:
        raise HTTPException(404, "Block not found")

    block.is_block = data.is_block
    block.approved_by = current_user.id

    db.commit()
    db.refresh(block)

    return block

@router.get("/check")
def check_block(
    date: date,
    user_id: int,
    db: Session = Depends(get_db)
):
    # Global block
    global_block = db.query(BlockTimesheet).filter(
        BlockTimesheet.timesheet_date == date,
        BlockTimesheet.user_id == 0,
        BlockTimesheet.is_block == True
    ).first()

    # User block
    user_block = db.query(BlockTimesheet).filter(
        BlockTimesheet.timesheet_date == date,
        BlockTimesheet.user_id == user_id,
        BlockTimesheet.is_block == True
    ).first()

    if global_block or user_block:
        return {"blocked": True}

    return {"blocked": False}