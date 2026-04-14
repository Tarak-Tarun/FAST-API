from fastapi import APIRouter #type: ignore
from routers.schemas.user_schema import Product #type: ignore
router = APIRouter()

@router.post("/products",status_code=201,response_model=Product)
def create_product(product: Product):
    return product
       