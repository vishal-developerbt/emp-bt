from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.db.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserUpdate, UserLogin, ChangePassword, ForgotPasswordRequest, ResetPassword
from app.core.security import hash_password, verify_password, create_access_token
from app.core.deps import get_current_user
from app.core.utils import generate_otp, generate_username

from datetime import datetime, timedelta
from app.models.login_history import LoginHistory
from fastapi import Request
from app.core.email.forgot_password import send_forgot_password_email
from app.core.email.reset_password import send_reset_success_email

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    
    # ✅ Check email exists
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    # ✅ Generate username
    username = generate_username(db)

    # ✅ Create user
    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role=user.role,            # ✅ ADD ROLE
        username=username          # ✅ ADD USERNAME
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User created successfully",
        "username": new_user.username,
        "role": new_user.role
    }

@router.get("/users", response_model=list[UserResponse])
def get_all_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    users = db.query(User).all()

    return users

@router.post("/login")
def login(user: UserLogin, request: Request, db: Session = Depends(get_db)):

    # 📌 Request info
    ip = request.client.host
    user_agent = request.headers.get("user-agent")

    # 🔍 Find user by email OR username
    db_user = db.query(User).filter(
        or_(
            User.email == user.identifier,
            User.username == user.identifier
        )
    ).first()

    # ❌ Invalid user OR password
    if not db_user or not verify_password(user.password, db_user.password):

        log = LoginHistory(
            user_id=db_user.id if db_user else None,
            email=db_user.email if db_user else user.identifier,
            ip_address=ip,
            user_agent=user_agent,
            status="Failed"
        )
        db.add(log)
        db.commit()

        raise HTTPException(status_code=401, detail="Invalid credentials")

    # ✅ Generate token
    token = create_access_token({
        "sub": str(db_user.id),
        "role": db_user.role,
        "type": "access"
    })

    # ✅ Success log
    log = LoginHistory(
        user_id=db_user.id,
        email=db_user.email,
        ip_address=ip,
        user_agent=user_agent,
        status="Success"
    )
    db.add(log)
    db.commit()

    return {
        "access_token": token,
        "token_type": "bearer",
        "username": db_user.username,
        "role": db_user.role
    }

@router.put("/change-password")
def change_password(
    data: ChangePassword,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # ✅ Always fetch fresh user from SAME session
    user = db.query(User).filter(User.id == current_user.id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # ✅ Check old password
    if not verify_password(data.old_password, user.password):
        raise HTTPException(status_code=400, detail="Old password is incorrect")

    # ✅ Prevent same password reuse
    if data.old_password == data.new_password:
        raise HTTPException(
            status_code=400,
            detail="New password must be different"
        )

    # ✅ Hash and update password
    user.password = hash_password(data.new_password)

    # ✅ Commit changes
    db.commit()

    return {"message": "Password updated successfully"}


@router.post("/forgot-password")
def forgot_password(data: ForgotPasswordRequest, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    otp = generate_otp()

    user.reset_otp = otp
    user.otp_expiry = datetime.utcnow() + timedelta(minutes=10)

    db.commit()

    # ✅ Send email
    send_forgot_password_email(user.email, otp)

    return {"message": "OTP sent to email"}


@router.post("/reset-password")
def reset_password(data: ResetPassword, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == data.email).first()

    if not user or user.reset_otp != data.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    if user.otp_expiry < datetime.utcnow():
        raise HTTPException(status_code=400, detail="OTP expired")

    # ✅ Update password
    user.password = hash_password(data.new_password)

    # ✅ Clear OTP
    user.reset_otp = None
    user.otp_expiry = None

    db.commit()

    # ✅ Send confirmation email
    send_reset_success_email(user.email, user.name)

    return {"message": "Password reset successful"}

@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Only admin can delete users
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    # Prevent admin from deleting self
    if current_user.id == user_id:
        raise HTTPException(
            status_code=400,
            detail="You cannot delete your own account"
        )

    # Find user
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Delete user
    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}

@router.put("/users/{id}")
def update_user(id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.name = user_data.name
    user.email = user_data.email
    user.role = user_data.role

    db.commit()
    db.refresh(user)

    return user

@router.get("/users/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Only admin can view user details
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role
    }