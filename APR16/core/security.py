from jose import jwt #type: ignore
from datetime import datetime, timedelta
from core.config import settings

ALGORITHM = "HS256"

def create_token(data: dict):
    data["exp"] = datetime.utcnow() + timedelta(minutes=30)
    return jwt.encode(data, settings.SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])