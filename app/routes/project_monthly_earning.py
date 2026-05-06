from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import date

from app.db.database import SessionLocal
from app.models.project_monthly_earning import ProjectMonthlyEarning
from app.models.project import Project
from app.schemas.project_monthly_earning import (
    EarningCreate,
    EarningUpdate,
    EarningResponse
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

@router.post("/", response_model=EarningResponse)
def create_earning(
    data: EarningCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    # Check project exists
    project = db.query(Project).filter(Project.id == data.project_id).first()
    if not project:
        raise HTTPException(404, "Project not found")

    month = normalize_month(data.month)

    existing = db.query(ProjectMonthlyEarning).filter(
        ProjectMonthlyEarning.project_id == data.project_id,
        ProjectMonthlyEarning.month == month
    ).first()

    if existing:
        raise HTTPException(400, "Earning already exists for this month")

    earning = ProjectMonthlyEarning(
        project_id=data.project_id,
        month=month,
        earning=data.earning
    )

    db.add(earning)
    db.commit()
    db.refresh(earning)

    return earning

@router.put("/{id}", response_model=EarningResponse)
def update_earning(
    id: int,
    data: EarningUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    earning = db.query(ProjectMonthlyEarning).filter(
        ProjectMonthlyEarning.id == id
    ).first()

    if not earning:
        raise HTTPException(404, "Record not found")

    if data.earning is not None:
        earning.earning = data.earning

    db.commit()
    db.refresh(earning)

    return earning

@router.get("/", response_model=list[EarningResponse])
def get_earnings(
    project_id: int | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(ProjectMonthlyEarning)

    if project_id:
        query = query.filter(ProjectMonthlyEarning.project_id == project_id)

    return query.order_by(ProjectMonthlyEarning.month.desc()).all()


@router.get("/project/{project_id}", response_model=list[EarningResponse])
def get_project_earnings(project_id: int, db: Session = Depends(get_db)):
    return db.query(ProjectMonthlyEarning).filter(
        ProjectMonthlyEarning.project_id == project_id
    ).order_by(ProjectMonthlyEarning.month.desc()).all()


@router.delete("/{id}")
def delete_earning(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(403, "Not authorized")

    earning = db.query(ProjectMonthlyEarning).filter(
        ProjectMonthlyEarning.id == id
    ).first()

    if not earning:
        raise HTTPException(404, "Record not found")

    db.delete(earning)
    db.commit()

    return {"message": "Deleted successfully"}