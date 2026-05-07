from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.db.database import SessionLocal
from app.models.employee_model import User
from app.schemas.employee_schema import (
    UserCreate, UserResponse, UserUpdate,
    UserLogin, ChangePassword
)
from app.core.security import hash_password, verify_password, create_access_token
from app.core.deps import get_current_user

from app.models.employee_model import LoginSession

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    # Check email
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(400, "Email already exists")

    # Check employee_code
    if db.query(User).filter(User.employee_code == user.employee_code).first():
        raise HTTPException(400, "Employee code already exists")

    new_user = User(
        name=user.name,
        employee_code=user.employee_code,
        email=user.email,
        password=hash_password(user.password),
        role=user.role,
        emp_shift_id=user.emp_shift_id,
        technology_id=user.technology_id
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}

@router.post("/login")
def login(user: UserLogin, request: Request, db: Session = Depends(get_db)):

    ip = request.client.host
    user_agent = request.headers.get("user-agent")

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user or not verify_password(user.password, db_user.password):

        db.add(LoginSession(
            user_id=db_user.id if db_user else None,
            email=user.email,
            ip_address=ip,
            user_agent=user_agent,
            status="Failed"
        ))
        db.commit()

        raise HTTPException(401, "Invalid credentials")

    token = create_access_token({
        "sub": str(db_user.id),
        "role": db_user.role
    })

    db.add(LoginSession(
        user_id=db_user.id,
        email=db_user.email,
        ip_address=ip,
        user_agent=user_agent,
        status="Success"
    ))
    db.commit()

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": db_user.role
    }

@router.get("/users", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    return db.query(User).order_by(User.id.desc()).all()


@router.get("/users", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    return db.query(User).order_by(User.id.desc()).all()

@router.put("/users/{id}", response_model=UserResponse)
def update_user(
    id: int,
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(404, "User not found")

    # Check email uniqueness
    if data.email:
        existing = db.query(User).filter(
            User.email == data.email,
            User.id != id
        ).first()
        if existing:
            raise HTTPException(400, "Email already in use")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)

    return user

@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    if current_user.id == user_id:
        raise HTTPException(400, "Cannot delete yourself")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(404, "User not found")

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}


@router.put("/change-password")
def change_password(
    data: ChangePassword,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = db.query(User).filter(User.id == current_user.id).first()

    if not verify_password(data.old_password, user.password):
        raise HTTPException(400, "Old password incorrect")

    user.password = hash_password(data.new_password)

    db.commit()

    return {"message": "Password updated"}