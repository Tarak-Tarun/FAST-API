from fastapi import FastAPI #type: ignore
from routers.User import router #type: ignore
from routers.products import router as product_router
app=FastAPI()
@app.get("/")
def read_root():
    return {"Hello":"World"}
app.include_router(router)
app.include_router(product_router)