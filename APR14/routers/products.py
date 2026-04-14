from fastapi import APIRouter #type: ignore
from schemas.product_schema import Product #type: ignore
router = APIRouter()
@router.post("/products")
def create_product(product: Product):
    return product
