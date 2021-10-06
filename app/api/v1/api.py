from fastapi import APIRouter

from app.api.v1.endpoints import collect

api_router = APIRouter()
api_router.include_router(collect.router, prefix="/collect")
