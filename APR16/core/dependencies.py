from fastapi.security import OAuth2PasswordBearer #type: ignore
from fastapi import Depends, HTTPException #type: ignore
from sqlalchemy.orm import Session #type: ignore
from core.security import decode_token
from db.database import get_db
from models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    try:
        data = decode_token(token)
        email = data["sub"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.email == email).first()
    return user

def admin_required(user = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")
    return user