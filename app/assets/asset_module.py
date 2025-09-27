from fastapi import APIRouter
from .asset_controller import router as asset_router

def asset_module() -> APIRouter:
    module = APIRouter()
    module.include_router(asset_router, prefix="/api", tags=["Assets"])
    return module
