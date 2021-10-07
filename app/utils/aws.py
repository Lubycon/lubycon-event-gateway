from app.core.config import settings

import boto3


async def get_session(region: str = settings.AWS_DEFAULT_REGION) -> any:
    if not settings.SERVER_STACK or settings.SERVER_STACK == settings.SERVER_STACK_LOCAL_NAME:
        # Local developments
        return boto3.Session(profile_name=settings.AWS_LOCAL_PROFILE, region_name=region)
    return boto3.Session(region_name=region)
