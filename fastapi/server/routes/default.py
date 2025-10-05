from fastapi import APIRouter, HTTPException, status


# router = APIRouter(prefix="/test", tags=["test"])
router = APIRouter(tags=["default"])

@router.get("/", summary="Service root")
async def root():
    return {"message": "fastapi-minimal is up", "docs": "/docs"}