from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.routes.auth import router as auth_router
from app.routes.profile import router as profile_router
from app.routes.timesheet import router as timesheet_router
from app.routes.dashboard import router as dashboard_router
#from app.routes.salary import router as salary_router
from app.routes.attendance import router as attendance_router
from app.routes.claim import router as claim_router
from app.routes.holiday import router as holiday_router
from app.routes.project import router as project_router
from app.routes import cms_image, login_session
from app.routes import role
from app.routes import skill_department
from app.routes import skills
from app.routes import technology
from app.routes import team_lead
from app.routes import managers
from app.routes import project_managers
from app.routes import emp_wfh
from app.routes import time_sheet_comments
from app.routes import emp_shift
from app.routes import emp_salary
from app.routes import emp_registration
from app.routes import emp_policy
from app.routes import emp_prev_employment
from app.routes import emp_per_address
from app.routes import emp_notice
from app.routes import emp_leave
from app.routes import emp_increment
from app.routes import emp_feedback
from app.routes import emp_family_details
from app.routes import emp_education    
from app.routes import emp_communication
from app.routes import emp_band
from app.routes import emp_address
from app.routes import emp_account
from app.routes import emp_account_details
from app.routes import email_template
from app.routes import block_timesheet
from app.routes import claim_image
from app.routes import cms
from app.routes import cms_image
from app.routes import document
from app.routes import department
from app.routes.project_monthly_earning import router as project_monthly_earning_router
from app.routes.client_master import router as client_master_router
from app.routes.sub_process import router as sub_process_router
from app.routes import process
from app.routes import emp_shortleave
from app.routes import emp_technology







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
app.include_router(profile_router, prefix="/profiles", tags=["Profiles"])
app.include_router(timesheet_router, prefix="/timesheet", tags=["Timesheet"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(attendance_router, prefix="/attendance", tags=["Attendance"])
app.include_router(claim_router, prefix="/claims", tags=["Claims"])
app.include_router(holiday_router, prefix="/holidays", tags=["Holidays"])
app.include_router(project_router, prefix="/projects", tags=["Projects"])
app.include_router(login_session.router, prefix="/login-session", tags=["Login session"])
app.include_router(role.router, prefix="/roles", tags=["Roles"])
app.include_router(skill_department.router,prefix="/skill-department", tags=["Skill Department"])
app.include_router(skills.router,prefix="/skills", tags=["Skills"])
app.include_router(technology.router,prefix="/technology", tags=["Technology"])
app.include_router(team_lead.router, prefix="/team-lead", tags=["Team Lead"])
app.include_router(managers.router, prefix="/managers", tags=["Managers"])
app.include_router(project_managers.router, prefix="/project-managers", tags=["Project Managers"])
app.include_router(emp_wfh.router, prefix="/wfh", tags=["WFH"])
app.include_router(time_sheet_comments.router, prefix="/timesheet-comments", tags=["Timesheet Comments"])   
app.include_router(emp_shift.router, prefix="/emp-shift", tags=["Emp Shift"])
app.include_router(emp_salary.router, prefix="/emp-salary", tags=["Emp Salary"])
app.include_router(emp_policy.router, prefix="/emp-policy", tags=["Emp Policy"])
app.include_router(emp_prev_employment.router, prefix="/prev-employment", tags=["Previous Employment"])
app.include_router(emp_per_address.router, prefix="/per-address", tags=["Permanent Address"])
app.include_router(emp_notice.router, prefix="/notice", tags=["Notice"])
app.include_router(emp_leave.router, prefix="/leave", tags=["Leave"])
app.include_router(emp_increment.router, prefix="/increment", tags=["Increment"])
app.include_router(emp_feedback.router, prefix="/feedback", tags=["Employee Feedback"])
app.include_router(emp_family_details.router, prefix="/family", tags=["Family Details"])
app.include_router(emp_education.router, prefix="/education", tags=["Education"])
app.include_router(emp_communication.router, prefix="/communication", tags=["Communication"])
app.include_router(emp_band.router, prefix="/emp-band", tags=["Employee Band"])
app.include_router(emp_address.router, prefix="/address", tags=["Current Address"])
app.include_router(emp_account.router, prefix="/account", tags=["Employee Account"])
app.include_router(emp_account_details.router, prefix="/account-details", tags=["Employee Account Details"])
app.include_router(email_template.router, prefix="/email-templates", tags=["Email Templates"])
app.include_router(block_timesheet.router, prefix="/timesheet-block", tags=["Timesheet Block"])
app.include_router(claim_image.router, prefix="/claim-images", tags=["Claim Images"])
app.include_router(cms.router, prefix="/cms", tags=["CMS"])
app.include_router(cms_image.router, prefix="/cms-images", tags=["CMS Images"])
app.include_router(document.router, prefix="/documents", tags=["Documents"])
app.include_router(department.router, prefix="/departments", tags=["Departments"])
app.include_router(project_monthly_earning_router, prefix="/project-earnings", tags=["Project Earnings"])
app.include_router(client_master_router, prefix="/clients", tags=["Client Master"])
app.include_router(emp_registration.router, prefix="/emp-registration", tags=["Employee Registration"])
app.include_router(process.router, prefix="/process", tags=["Process"])
app.include_router(sub_process_router, prefix="/sub-processes", tags=["Sub Processes"])
app.include_router(emp_shortleave.router, prefix="/short-leave", tags=["Short Leave"])
app.include_router(emp_technology.router, prefix="/emp-technology", tags=["Employee Technology"])






@app.get("/")
def home():
    return {"message": "MyBlueThink API Running"}