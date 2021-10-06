from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/v1"
    PROJECT_NAME: str = "lubycon-event-gateway"

    SERVER_NAME: str = "event-gateway"
    SERVER_HOST: AnyHttpUrl = "http://localhost:8000"
    # SENTRY_DSN: Optional[HttpUrl] = None

    # @validator("SENTRY_DSN", pre=True)
    # def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
    #     if len(v) == 0:
    #         return None
    #     return v


settings = Settings()
