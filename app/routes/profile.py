from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserProfile, UpdateProfile
from app.core.deps import get_db, get_current_user

router = APIRouter()

# Get Profile
@router.get("/me", response_model=UserProfile)
def get_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return current_user


# Update Profile
@router.put("/me")
def update_profile(
    data: UpdateProfile,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    for key, value in data.dict(exclude_unset=True).items():
        setattr(current_user, key, value)

    db.commit()
    db.refresh(current_user)

    return {"message": "Profile updated"}