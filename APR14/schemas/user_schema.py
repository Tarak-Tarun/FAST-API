from pydantic import BaseModel, EmailStr, Field, field_validator

class Address(BaseModel):
    city: str
    pincode: int
    state: str

class Users(BaseModel):
    name: str
    age: int
    email: EmailStr
    phone: str = Field(min_length=10, max_length=10)
    address: Address

    @field_validator("name")
    def name_validator(cls, value):
        if not value.replace(" ", "").isalpha():
            raise ValueError("Name must contain only letters")
        return value

    @field_validator("age")
    def age_validator(cls, value):
        if value < 21:
            raise ValueError("User must be at least 21 for full access")
        return value

    @field_validator("phone")
    def phone_validator(cls, value):
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")
        return value