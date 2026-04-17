from fastapi import APIRouter, Depends #type: ignore
from sqlalchemy.orm import Session  #type: ignore
from schemas.product import ProductCreate
from models.product import Product
from db.database import get_db
from core.dependencies import admin_required, get_current_user

router = APIRouter(prefix="/products")

# anyone logged in
@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

# admin only
@router.post("/")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    user = Depends(admin_required)
):
    new_product = Product(name=product.name)
    db.add(new_product)
    db.commit()
    return new_product