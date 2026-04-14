from pydantic import field_validator,BaseModel #type: ignore
from  typing import Optional
class Address(BaseModel):
    city:str
    pincode:int
    state:str

class Product(BaseModel):
    name:str
    price:float
    quantity:int
    address:Address
    description:Optional[str]=None
    @field_validator("name")
    def name_validator(cls,value):
        if not value.replace(" ","").isalpha():
            raise ValueError("Name must contain only letters")
        return value
