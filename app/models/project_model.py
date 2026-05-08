from sqlalchemy import (
    Column, BigInteger, Text, String, Date, Boolean, SmallInteger,
    TIMESTAMP, Integer, Float, DateTime, UniqueConstraint, ForeignKey, JSON
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime
import uuid


# =========================
# PROJECT
# =========================
class Project(Base):
    __tablename__ = "projects"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    project_name = Column(String(255), nullable=False)
    vendor_name = Column(String(255), nullable=False)

    project_startdate = Column(Date, nullable=False)
    project_enddate = Column(Date, nullable=True)

    status = Column(Boolean, default=True)
    is_billable = Column(SmallInteger, default=1)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())


# =========================
# MANAGER
# =========================
class Manager(Base):
    __tablename__ = "managers"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    manager_name = Column(String(255), nullable=False)
    skill_type = Column(String(255), nullable=True)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())


# =========================
# TEAM LEAD
# =========================
class TeamLead(Base):
    __tablename__ = "team_lead"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    manager_id = Column(BigInteger, nullable=True)
    teamlead_id = Column(BigInteger, nullable=True)
    user_id = Column(BigInteger, nullable=True)

    status = Column(Boolean, default=False)  # 0/1 converted to bool

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())


# =========================
# PROJECT MANAGER
# =========================
class ProjectManager(Base):
    __tablename__ = "project_managers"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    project_id = Column(BigInteger, ForeignKey("projects.id"), nullable=False)
    manager_id = Column(BigInteger, nullable=False)
    developer_id = Column(BigInteger, nullable=False)
    technology_id = Column(BigInteger, nullable=False)

    status = Column(Boolean, default=True)
    resource_type = Column(Boolean, default=False)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())


# =========================
# PROJECT EARNING
# =========================
class ProjectMonthlyEarning(Base):
    __tablename__ = "project_monthly_earning"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    project_id = Column(BigInteger, ForeignKey("projects.id"), nullable=False)
    month = Column(Date, nullable=False)
    earning = Column(Float, nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('project_id', 'month', name='unique_project_month'),
    )


# =========================
# TECHNOLOGY
# =========================
class Technology(Base):
    __tablename__ = "technology"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    technology = Column(String(100), nullable=True)
    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())


# =========================
# SKILL
# =========================
class Skill(Base):
    __tablename__ = "skills"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    skill_name = Column(String(255), nullable=False)
    user_id = Column(BigInteger, nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())


# =========================
# SKILL DEPARTMENT
# =========================
class SkillDepartment(Base):
    __tablename__ = "skill_department"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    skill_name = Column(String(255), nullable=False)

    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())


# =========================
# CLIENT MASTER
# =========================
class ClientMaster(Base):
    __tablename__ = "client_master_list"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    technology = Column(String(255), nullable=True)
    interview_date = Column(String(255), nullable=True)

    company = Column(String(255), nullable=True)
    name = Column(String(255), nullable=True)

    contact_person = Column(String(255), nullable=True)
    client_email = Column(String(255), nullable=True)
    contact_number = Column(String(255), nullable=True)

    source = Column(String(255), nullable=True)
    rate = Column(String(255), nullable=True)

    pre_call_notes = Column(Text, nullable=True)
    meeting_link = Column(Text, nullable=True)
    post_call_notes = Column(Text, nullable=True)

    status = Column(Text, nullable=True)

    interview_taken_by = Column(String(255), nullable=True)
    end_client = Column(String(255), nullable=True)
    interview_type = Column(String(255), nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())


# =========================
# PROCESS
# =========================
class Process(Base):
    __tablename__ = "process"

    id = Column(String(255), primary_key=True, index=True)

    created_by = Column(String(255), nullable=True)
    creation_date = Column(DateTime, default=datetime.utcnow)

    last_modified_by = Column(String(255), nullable=True)
    last_modified_date = Column(DateTime, onupdate=datetime.utcnow)

    client = Column(String(255), nullable=True)
    client_cell = Column(String(255), nullable=True)
    client_email = Column(String(255), nullable=True)
    client_poc = Column(String(255), nullable=True)

    data_source = Column(String(255), nullable=True)

    properties = Column(JSON, nullable=True)

    rate = Column(String(255), nullable=True)
    source = Column(String(255), nullable=True)
    status = Column(String(255), nullable=True)

    candidate_id = Column(String(255), ForeignKey("profile.id"), nullable=True)

    consultant = Column(String(255), nullable=True)
    contact_id = Column(String(255), nullable=True)

    tags = Column(String(255), default="NOT TAGGED")


# =========================
# SUB PROCESS
# =========================
class SubProcess(Base):
    __tablename__ = "sub_process"

    id = Column(String(255), primary_key=True, index=True)

    created_by = Column(String(255), nullable=True)
    creation_date = Column(DateTime, default=datetime.utcnow)

    last_modified_by = Column(String(255), nullable=True)
    last_modified_date = Column(DateTime, onupdate=datetime.utcnow)

    client_cell = Column(String(255), nullable=True)
    client_email = Column(String(255), nullable=True)

    interview_date = Column(String(255), nullable=False)
    interview_mode = Column(String(255), nullable=True)
    interview_panel = Column(String(255), nullable=True)

    meeting_invite = Column(Text, nullable=True)
    note = Column(Text, nullable=True)

    properties = Column(JSON, nullable=True)

    status = Column(String(255), nullable=True)
    time = Column(String(255), nullable=True)

    consultant_id = Column(String(255), ForeignKey("profile.id"), nullable=True)
    process_id = Column(String(255), ForeignKey("process.id"), nullable=True)

    profile = Column(String(255), nullable=True)


# =========================
# DEPARTMENT
# =========================
class Department(Base):
    __tablename__ = "department"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    department_name = Column(String(255), nullable=False)
    status = Column(Boolean, default=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('department_name', name='unique_department_name'),
    )


# =========================
# DOCUMENT
# =========================
class Document(Base):
    __tablename__ = "document"

    id = Column(String(255), primary_key=True, default=lambda: str(uuid.uuid4()))

    classification = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)

    document = Column(String(255), nullable=True)

    name = Column(String(255), nullable=True)

    process_id = Column(String(255), nullable=True)
    profile_id = Column(String(255), nullable=True)
    sub_process_id = Column(String(255), nullable=True)

    tags = Column(String(255), nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())