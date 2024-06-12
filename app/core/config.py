from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "rag-api"

    API_V1_STR: str = "/api/v1"

    class Config:
        case_sensitive = True


settings = Settings()
