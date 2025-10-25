import uuid
from fastapi import APIRouter, HTTPException, status,Depends,Query
from schemas.inventory_schema import InventoryCreate,InventoryRead
from models.db import get_write_session,get_read_session
from models import Inventory
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,desc, asc
from typing import List,Optional

inventory_router =APIRouter(tags=["inventory"])

""" create """
@inventory_router.post("/",
                response_model=InventoryRead, 
                status_code=status.HTTP_201_CREATED, 
                summary="Create Inventory")
async def create_item(payload: InventoryCreate,session:AsyncSession = Depends(get_write_session)):
        new_inventory = Inventory(
            id=str(uuid.uuid4()),
            name=payload.name,
            model_no=payload.model_no,
            price=payload.price,
            qty=payload.qty
        )
        try:  
            session.add(new_inventory)
            await session.commit()
            await session.refresh(new_inventory)
            return new_inventory
        except IntegrityError as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Inventory with this model number already exists."
            )
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Unexpected error: {str(e)}"
            )

""" get one """
@inventory_router.get("/{id}", response_model=InventoryRead, summary="Get Inventory by ID")
async def get_item(id: str, session: AsyncSession = Depends(get_read_session)):
    item = await session.get(Inventory, id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found.")
    return item

""" update """
@inventory_router.put("/{id}", response_model=InventoryRead, summary="Update Inventory by ID")
async def update_item(id: str, payload: InventoryCreate, session: AsyncSession = Depends(get_write_session)):
    item = await session.get(Inventory, id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found.")
    item.name = payload.name
    item.model_no = payload.model_no
    item.price = payload.price
    item.qty = payload.qty
    try:
        await session.commit()
        await session.refresh(item)
        return item
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Model number already exists.")
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")


""" delte """
@inventory_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Inventory by ID")
async def delete_item(id: str, session: AsyncSession = Depends(get_write_session)):
    item = await session.get(Inventory, id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found.")
    await session.delete(item)
    await session.commit()


@inventory_router.get(
    "/",
    response_model=List[InventoryRead],
    summary="List all inventory (no pagination)"
)
async def list_inventory(session: AsyncSession = Depends(get_read_session)):
    try:
        stmt = select(Inventory)
        result = await session.execute(stmt)
        items = result.scalars().all()
        return items
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(e)}"
        )

@inventory_router.get(
    "/page1",
    response_model=List[InventoryRead],
    summary="List all inventory",
)
async def list_inventory(
    limit: int = Query(50, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    sort_by: Optional[str] = Query("createdAt"),
    sort_dir: Optional[str] = Query("desc"),
    session: AsyncSession = Depends(get_read_session),
):
    try:
        # choose sort column safely (avoid SQL injection by whitelisting)
        allowed_sort_columns = {"created_at": Inventory.created_at, "updated_at": Inventory.updated_at, "price": Inventory.price, "name": Inventory.name, "model_no": Inventory.model_no}
        sort_col = allowed_sort_columns.get(sort_by, Inventory.created_at)

        order = desc(sort_col) if sort_dir.lower() == "desc" else asc(sort_col)

        stmt = select(Inventory).order_by(order).limit(limit).offset(offset)
        result = await session.execute(stmt)
        items = result.scalars().all()
        return items
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")
