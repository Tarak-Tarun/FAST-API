from pydantic import BaseModel, Field #type: ignore
class User(BaseModel):
    name:str=Field(min_length=3,max_length=50)
    email:str =Field(min_length=5,max_length=50)
    age:int=Field(gt=0,lt=120)

