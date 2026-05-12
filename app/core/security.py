from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import bcrypt

# Config
SECRET_KEY = "mysupersecretkey123456"
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60
REFRESH_TOKEN_EXPIRE_DAYS = 7

# Password Hashing
#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(
        password.encode("utf-8"),
        salt
    )

    return hashed.decode("utf-8")


import bcrypt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )

# Create Access Token
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({
        "exp": expire,
        "type": "access"
    })

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# Create Refresh Token
def create_refresh_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)

    to_encode.update({
        "exp": expire,
        "type": "refresh"
    })

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)