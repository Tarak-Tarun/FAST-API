from pydantic_settings import BaseSettings #type: ignore

class Settings(BaseSettings):
    SECRET_KEY: str
    DATABASE_URL: str   # ✅ MUST be here

    class Config:
        env_file = ".env"
        extra = "ignore"   # 🔥 important fix

settings = Settings()