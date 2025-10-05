from fastapi import APIRouter, HTTPException, status
from server_config import server_path

# router = APIRouter(prefix="/test", tags=["test"])
router = APIRouter(tags=["default"])

@router.get("/", summary="Service root")
async def root():
    return {"message": "fastapi is up", "server_path": server_path}