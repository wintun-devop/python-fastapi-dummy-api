from fastapi import APIRouter, HTTPException, status
from constants.dummy import _Dummies
from schema.dummy_schema import Dummy,DummyUpdate

dummy_router =APIRouter(tags=["dummy"])

""" create """
@dummy_router.post("/", response_model=Dummy, status_code=status.HTTP_201_CREATED, summary="Create dummy")
async def create_item(item: Dummy):
    if item.id in _Dummies:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    _Dummies[item.id] = item
    return item

""" read """
@dummy_router.get("/", response_model=list[Dummy], summary="List dummies")
async def list_items():
    return list(_Dummies.values())

@dummy_router.get("/{id}", response_model=Dummy, summary="Get dummy by id")
async def get_item(id: str):
    item = _Dummies.get(id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item
""" update """
@dummy_router.patch("/partial/{id}", response_model=Dummy, summary="Update item partially")
async def update_item(id: str, patch: DummyUpdate):
    existing = _Dummies.get(id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    updated = existing.model_copy(update=patch.model_dump(exclude_unset=True))
    _Dummies[id] = updated
    return updated

@dummy_router.put("/{id}", response_model=Dummy, summary="Replace item")
async def replace_item(id: str, item: Dummy):
    if id != item.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID mismatch")
    if id not in _Dummies:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    _Dummies[id] = item
    return item

""" delete """
@dummy_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete item")
async def delete_item(id: str):
    if id not in _Dummies:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    del _Dummies[id]
    return None