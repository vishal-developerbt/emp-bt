from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.claim import Claim
from app.schemas.claim import (
    ClaimCreate,
    ClaimUpdate,
    ClaimResponse
)
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
VALID_CATEGORIES = ["Mobile", "Broadband", "TravelAllowance", "Other"]
VALID_STATUS = ["Pending", "Approve", "Reject"]

@router.post("/", response_model=ClaimResponse)
def create_claim(
    data: ClaimCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if data.category not in VALID_CATEGORIES:
        raise HTTPException(400, "Invalid category")

    if data.start_date > data.end_date:
        raise HTTPException(400, "Invalid date range")

    if data.category == "Mobile" and not data.mobile:
        raise HTTPException(400, "Mobile number required")

    claim = Claim(
        **data.dict(),
        user_id=current_user.id
    )

    db.add(claim)
    db.commit()
    db.refresh(claim)

    return claim


@router.put("/{id}", response_model=ClaimResponse)
def update_claim(
    id: int,
    data: ClaimUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    claim = db.query(Claim).filter(
        Claim.id == id,
        Claim.user_id == current_user.id
    ).first()

    if not claim:
        raise HTTPException(404, "Claim not found")

    if claim.status != "Pending":
        raise HTTPException(400, "Cannot edit processed claim")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(claim, field, value)

    db.commit()
    db.refresh(claim)

    return claim

@router.get("/", response_model=list[ClaimResponse])
def get_my_claims(
    status: str | None = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Claim).filter(Claim.user_id == current_user.id)

    if status:
        query = query.filter(Claim.status == status)

    return query.order_by(Claim.id.desc()).all()

@router.put("/approve/{id}")
def approve_claim(
    id: int,
    status: str = Query(...),
    comment: str = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role not in ["admin", "manager"]:
        raise HTTPException(403, "Not authorized")

    if status not in VALID_STATUS:
        raise HTTPException(400, "Invalid status")

    claim = db.query(Claim).filter(Claim.id == id).first()

    if not claim:
        raise HTTPException(404, "Claim not found")

    claim.status = status
    claim.approval_by = current_user.id
    claim.manager_comment = comment

    db.commit()

    return {"message": f"Claim {status}"}