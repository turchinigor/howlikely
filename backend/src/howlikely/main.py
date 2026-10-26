"""FastAPI entry point. Run with: uvicorn howlikely.main:app --reload"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from howlikely import __version__
from howlikely.api.routes import health
from howlikely.config import settings

app = FastAPI(title="HowLikely API", version=__version__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/v1")
