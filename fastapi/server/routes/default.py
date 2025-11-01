from fastapi import APIRouter


# router = APIRouter(prefix="/test", tags=["test"])
router = APIRouter(tags=["default"])

@router.get("/", summary="Service root")
async def root():
    return {"message": "fastapi is up"}