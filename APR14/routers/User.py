from fastapi import APIRouter #type: ignore
from schemas.user_schema import Product #type: ignore
router = APIRouter()
@router.post("/prodcuts",status_code=201,response_model=Product)
def products(product: Product):
    return product
