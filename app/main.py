from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.routes.auth import router as auth_router
from app.routes.profile import router as profile_router
from app.routes.timesheet import router as timesheet_router
from app.routes.leave import router as leave_router
from app.routes.dashboard import router as dashboard_router
from app.routes.salary import router as salary_router
from app.routes.attendance import router as attendance_router
from app.routes.claim import router as claim_router
from app.routes.holiday import router as holiday_router
from app.routes.project import router as project_router
from app.routes import login_history
from app.routes import role
from app.routes import skill_department
from app.routes import skills
from app.routes import technology
from app.routes import team_lead
from app.routes import managers
from app.routes import project_managers


# Create FastAPI app FIRST
app = FastAPI(
    title="MyBlueThink API",
    version="1.0.0"
)

# Add middleware AFTER app creation
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(profile_router, prefix="/profile", tags=["Profile"])
app.include_router(timesheet_router, prefix="/timesheet", tags=["Timesheet"])
app.include_router(leave_router, prefix="/leave", tags=["Leave"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(salary_router, prefix="/salary", tags=["Salary"])
app.include_router(attendance_router, prefix="/attendance", tags=["Attendance"])
app.include_router(claim_router, prefix="/claim", tags=["Claim"])
app.include_router(holiday_router, prefix="/holiday", tags=["Holiday"])
app.include_router(project_router, prefix="/project", tags=["Project"])
app.include_router(login_history.router, prefix="/login-history", tags=["Login History"])
app.include_router(role.router, prefix="/role", tags=["Role"])
app.include_router(skill_department.router,prefix="/skill-department", tags=["Skill Department"])
app.include_router(skills.router,prefix="/skills", tags=["Skills"])
app.include_router(technology.router,prefix="/technology", tags=["Technology"])
app.include_router(team_lead.router, prefix="/team-lead", tags=["Team Lead"])
app.include_router(managers.router, prefix="/managers", tags=["Managers"])
app.include_router(project_managers.router, prefix="/project-managers", tags=["Project Managers"])


@app.get("/")
def home():
    return {"message": "MyBlueThink API Running"}