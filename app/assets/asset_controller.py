from fastapi import APIRouter, Depends
from .asset_service import AssetService

router = APIRouter()

def get_asset_service():
    return AssetService()

@router.get("/asset")
def get_hello(service: AssetService = Depends(get_asset_service)):
    return {"message": service.get_message()}
