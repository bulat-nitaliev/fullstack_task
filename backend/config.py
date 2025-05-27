from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    DB_DRIVER: str = "postgresql+asyncpg"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"
    DB_NAME: str = "task"
    # TEST_DB_NAME: str = "test_pomodor"
    CACHE_HOST: str = "localhost"
    CACHE_PORT: int = 6379
    CACHE_DB: int = 0
    # TEST_CACHE_HOST: str = "localhost"
    # TEST_CACHE_PORT: int = 6379
    # TEST_CACHE_DB: int = 1

    @property
    def get_db_url(self):
        return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def get_test_db_url(self):
        return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.TEST_DB_NAME}"


settings = Settings()
