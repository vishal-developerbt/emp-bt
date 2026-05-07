from datetime import datetime
from app.models.employee_model import User
from dateutil.relativedelta import relativedelta
import random
import re


def generate_username(db):
    year = datetime.now().year

    last_user = db.query(User)\
        .filter(User.username.like(f"AV{year}%"))\
        .order_by(User.id.desc())\
        .first()

    if last_user:
        last_number = int(last_user.username[-3:])
        new_number = last_number + 1
    else:
        new_number = 1

    return f"AV{year}{str(new_number).zfill(3)}"


def generate_otp():
    return str(random.randint(100000, 999999))


def calculate_next_increment(increment_date, interval_months):
    if not increment_date:
        return None

    return increment_date + relativedelta(months=interval_months)


def validate_aadhaar(aadhaar: str):
    return aadhaar.isdigit() and len(aadhaar) == 12

def validate_pan(pan: str):
    return bool(re.match(r"[A-Z]{5}[0-9]{4}[A-Z]{1}", pan))

def validate_ifsc(ifsc: str):
    return bool(re.match(r"^[A-Z]{4}0[A-Z0-9]{6}$", ifsc))

def validate_account(acc_no: str):
    return acc_no.isdigit() and 8 <= len(acc_no) <= 18