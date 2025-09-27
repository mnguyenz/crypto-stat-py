from fastapi import FastAPI
from app.assets.asset_module import asset_module

app = FastAPI(title="FastAPI NestJS-like Project")

# Import Hello module
app.include_router(asset_module())