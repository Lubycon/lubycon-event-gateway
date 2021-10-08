from fastapi import FastAPI
from mangum import Mangum
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core.config import settings
from app.worker.consumer import handler

app = FastAPI(title=settings.PROJECT_NAME)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)
api_handler = Mangum(app)
worker_handler = handler
