from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserLogin
from services.auth_service import create_user, get_user
from core.security import create_token
from db.database import get_db
from core.dependencies import get_current_user

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.email, user.password)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user(db, user.email)

    if not db_user or db_user.password != user.password:
        return {"error": "Invalid credentials"}

    token = create_token({"sub": db_user.email})
    return {"access_token": token}

@router.get("/me")
def get_me(user = Depends(get_current_user)):
    return {"email": user.email, "role": user.role}