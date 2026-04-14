from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional

class Address(BaseModel):
    city: str
    pincode: int
    state: str

class Product(BaseModel):
    name: str
    price: float = Field(ge=100)
    quantity: int = Field(ge=1)
    description: Optional[str] = None
    address: Address

    @field_validator("name")
    def name_validator(cls, value):
        if not value.replace(" ", "").isalpha():
            raise ValueError("Name must contain only letters and spaces")
        return value

    @model_validator(mode="after")
    def price_validator(self):
        if self.price * self.quantity < 500:
            raise ValueError("Total must be at least 500")
        return self
    