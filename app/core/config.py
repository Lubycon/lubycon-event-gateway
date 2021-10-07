import os

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):
    API_V1_STR: str = '/v1'
    PROJECT_NAME: str = 'lubycon-event-gateway'

    SERVER_NAME: str = 'event-gateway'
    SERVER_HOST: AnyHttpUrl = 'http://localhost:8000'
    SERVER_STACK_LOCAL_NAME: str = 'local'
    SERVER_STACK: str = os.getenv('STAGE', SERVER_STACK_LOCAL_NAME)

    AWS_LOCAL_PROFILE: str = 'lubycon-mgmt'
    AWS_DEFAULT_REGION: str = os.getenv('REGION', 'ap-northeast-2')
    # TODO : Terraform에서 생성한 test queue로 변경?
    AWS_EVENT_LOG_SQS_URL: str = os.getenv('AWS_EVENT_LOG_SQS_URL', 'https://sqs.ap-northeast-2.amazonaws.com/554707519121/test-queue')
    # SENTRY_DSN: Optional[HttpUrl] = None

    # @validator('SENTRY_DSN', pre=True)
    # def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
    #     if len(v) == 0:
    #         return None
    #     return v


settings = Settings()
