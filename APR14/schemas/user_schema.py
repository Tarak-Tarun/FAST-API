from pydantic import BaseModel, Field,model_validator  #type: ignore
class Product(BaseModel):
    name: str = Field(min_length=3)
    price:int=Field(ge=100)
    quantity:int=Field(ge=1)
    @model_validator(mode="before")
    def before_validation(cls,values):
        values["name"]=values.get("name").upper()
        return values
    @model_validator(mode="after")
    def after_validation(self):
        if self.price < 100:
            raise ValueError("Price must be at least 100")
        return self

