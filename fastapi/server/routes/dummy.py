from fastapi import APIRouter, HTTPException, status
from constants.dummy import _Dummies
from schema.dummy_schema import Dummy

dummy_router =APIRouter(tags=["dummy"])

@dummy_router.get("/", response_model=list[Dummy], summary="List dummies")
async def list_items():
    return list(_Dummies.values())