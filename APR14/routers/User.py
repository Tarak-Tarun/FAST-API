from fastapi import APIRouter #type: ignore
from schemas.user_schema import User #type: ignore
router = APIRouter()
@router.post("/users",status_code=201,response_model=User)
def create_user(user: User):
    return user
