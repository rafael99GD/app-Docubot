from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    telegram_bot_token: str
    gemini_api_key: str
    database_url: str = "postgresql://docubot:docubot@localhost:5432/docubot"

    class Config:
        env_file = ".env"


settings = Settings()
