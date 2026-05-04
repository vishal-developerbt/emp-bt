from datetime import datetime
from app.models.user import User
import random

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