from fastapi import APIRouter #type: ignore
from schemas.user_schema import Users #type: ignore
router = APIRouter()
@router.post("/users")
def create_user(user: Users):
    return user
