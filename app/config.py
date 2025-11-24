from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./tasks.db"
    secret_key: str = "replace-this-with-a-secure-random-string"
    access_token_expire_minutes: int = 60

    class Config:
        env_file = ".env"


settings = Settings()
