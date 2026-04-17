from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, product
from db.database import Base, engine

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(product.router)