from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.salary import Salary
from app.models.user import User
from app.core.deps import get_current_user
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/slip")
def generate_salary_slip(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    salary = db.query(Salary).filter(
        Salary.user_id == current_user.id
    ).first()

    if not salary:
        raise HTTPException(status_code=404, detail="Salary not found")

    file_path = f"salary_{current_user.id}.pdf"

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph(f"Salary Slip - {salary.month}", styles["Title"]))
    elements.append(Paragraph(f"Name: {current_user.name}", styles["Normal"]))
    elements.append(Paragraph(f"Email: {current_user.email}", styles["Normal"]))

    elements.append(Paragraph(f"Basic: {salary.basic}", styles["Normal"]))
    elements.append(Paragraph(f"HRA: {salary.hra}", styles["Normal"]))
    elements.append(Paragraph(f"Bonus: {salary.bonus}", styles["Normal"]))
    elements.append(Paragraph(f"Deductions: {salary.deductions}", styles["Normal"]))

    total = salary.basic + salary.hra + salary.bonus - salary.deductions
    elements.append(Paragraph(f"Net Salary: {total}", styles["Heading2"]))

    doc.build(elements)

    return FileResponse(file_path, media_type='application/pdf', filename=file_path)