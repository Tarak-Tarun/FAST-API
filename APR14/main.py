from fastapi import FastAPI #type: ignore
from routers.User import router #type: ignore
app=FastAPI()
@app.get("/")
def read_root():
    return {"Hello":"World"}
app.include_router(router)