from sqlalchemy import create_engine #type: ignore
from sqlalchemy.orm import sessionmaker, DeclarativeBase #type: ignore
from core.config import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()