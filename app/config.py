from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    DATABASE_HOST: str = "localhost"
    DATABASE_NAME: str = Field(..., env="DATABASE_NAME")
    DATABASE_USER: str = Field(..., env="DATABASE_USER")
    DATABASE_PASSWORD: str = Field(..., env="DATABASE_PASSWORD")

settings = Settings()