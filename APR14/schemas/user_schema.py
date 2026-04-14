from pydantic import BaseModel, Field #type: ignore
class Product(BaseModel):
    name: str = Field(min_length=3)
    price:int=Field(ge=100)
    quantity:int=Field(ge=1)