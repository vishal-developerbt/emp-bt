from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.project import Project
from app.models.assigned_project import AssignedProject
from app.models.user import User
from app.core.deps import get_current_user
from app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
    AssignProjectRequest
)
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Project (Admin)
@router.post("/", response_model=ProjectResponse)
def create_project(
    data: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    project = Project(**data.dict())
    db.add(project)
    db.commit()
    db.refresh(project)

    return project


# Assign Project to User
# @router.post("/assign")
# def assign_project(
#     user_id: int,
#     project_id: int,
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user)
# ):
#     if current_user.role != "admin":
#         raise HTTPException(status_code=403, detail="Not authorized")

#     assignment = AssignedProject(
#         user_id=user_id,
#         project_id=project_id
#     )

#     db.add(assignment)
#     db.commit()

#     return {"message": "Project assigned successfully"}

# Assign Project to User by Username
@router.post("/assign")
def assign_project(
    request: AssignProjectRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Only admin can assign
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    # Find employee/user by username
    user = db.query(User).filter(User.username == request.username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if project exists
    project = db.query(Project).filter(
        Project.id == request.project_id
    ).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # Check if project manager exists
    manager = db.query(User).filter(
        User.id == request.project_manager_user_id
    ).first()

    if not manager:
        raise HTTPException(status_code=404, detail="Project manager not found")

    # Prevent duplicate assignment
    existing_assignment = db.query(AssignedProject).filter(
        AssignedProject.user_id == user.id,
        AssignedProject.project_id == request.project_id
    ).first()

    if existing_assignment:
        raise HTTPException(
            status_code=400,
            detail="Project already assigned"
        )

    # Create assignment
    assignment = AssignedProject(
        user_id=user.id,
        project_id=request.project_id,
        project_manager_user_id=request.project_manager_user_id,
        project_start_date=request.project_start_date
    )

    db.add(assignment)
    db.commit()
    db.refresh(assignment)

    return {
        "message": "Project assigned successfully",
        "assigned_to": user.username,
        "project_id": request.project_id,
        "project_manager_user_id": request.project_manager_user_id
    }

# Get All Projects
@router.get("/all", response_model=list[ProjectResponse])
def get_all_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Optional: restrict only admin
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    projects = db.query(Project).all()

    return projects

# Get My Projects
@router.get("/my")
def get_my_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    print("TESTing")
    assignments = db.query(AssignedProject).filter(
        AssignedProject.user_id == current_user.id
    ).all()

    project_ids = [a.project_id for a in assignments]

    projects = db.query(Project).filter(Project.id.in_(project_ids)).all()

    return projects

@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project

@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(
    project_id: int,
    data: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    for key, value in data.dict().items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)

    return project

@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(project)
    db.commit()

    return {"message": "Project deleted successfully"}