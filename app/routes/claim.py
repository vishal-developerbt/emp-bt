from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.claim import Claim
from app.models.user import User
from app.schemas.claim import ClaimCreate, ClaimResponse
from app.core.deps import get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Claim
@router.post("/", response_model=ClaimResponse)
def create_claim(
    data: ClaimCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    claim = Claim(
        user_id=current_user.id,
        title=data.title,
        amount=data.amount,
        description=data.description
    )

    db.add(claim)
    db.commit()
    db.refresh(claim)

    return claim


# Get My Claims
@router.get("/", response_model=list[ClaimResponse])
def get_claims(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Claim).filter(
        Claim.user_id == current_user.id
    ).all()


# Admin Approve / Reject
@router.put("/approve/{id}")
def approve_claim(
    id: int,
    status: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    claim = db.query(Claim).filter(Claim.id == id).first()

    if not claim:
        raise HTTPException(status_code=404, detail="Not found")

    if status not in ["Approved", "Rejected"]:
        raise HTTPException(status_code=400, detail="Invalid status")

    claim.status = status
    db.commit()

    return {"message": f"Claim {status}"}