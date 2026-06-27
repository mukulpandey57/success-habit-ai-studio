from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Success Habit AI Studio"
    VERSION: str = "1.0.0"
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    OLLAMA_URL: str = "http://localhost:11434"

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()