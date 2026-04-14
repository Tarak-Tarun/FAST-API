from fastapi import APIRouter #type: ignore
from schemas.user_schema import Product #type: ignore
router = APIRouter()
@router.post("/prodcuts")
def products(product: Product):
    return product
