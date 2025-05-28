from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    DB_DRIVER: str = "postgresql+asyncpg"
    DB_HOST: str = "db"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"
    DB_NAME: str = "task"
    CACHE_HOST: str = "cache"
    CACHE_PORT: int = 6379
    CACHE_DB: int = 0

    @property
    def get_db_url(self):
        return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

   
settings = Settings()
