from fastapi import FastAPI #type: ignore
from APR13.routers.sample import router as sample_router
app=FastAPI()
app.include_router(sample_router)
