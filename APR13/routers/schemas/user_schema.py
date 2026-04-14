from pydantic import BaseModel #type: ignore
class Product(BaseModel):
    name:str
    price:int
    quantity:int