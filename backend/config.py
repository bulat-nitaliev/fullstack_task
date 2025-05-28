from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    DB_DRIVER: str = "postgresql+asyncpg"
    DB_HOST: str = "0.0.0.0"
    DB_PORT: str = "5433"
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"
    DB_NAME: str = "task"
    CACHE_HOST: str = "0.0.0.0"
    CACHE_PORT: int = 6377
    CACHE_DB: int = 0

    @property
    def get_db_url(self):
        return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

   
settings = Settings()
