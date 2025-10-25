from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from server.models import Inventory

async def inventory_create(session: AsyncSession, data:Inventory) -> Inventory:
    inventory = Inventory(**data)
    session.add(inventory)
    await session.commit()
    await session.refresh(inventory)
    return inventory


async def inventory_get_one(session:AsyncSession,id:str)->Inventory | None:
    result = await session.execute(select(Inventory).where(Inventory.id == id))
    return result.scalar_one_or_none()

async def inventory_update(session: AsyncSession, id: str, data: dict) -> Inventory | None:
    result = await session.execute(select(Inventory).where(Inventory.id == id))
    inventory = result.scalar_one_or_none()
    if not inventory:
        return None
    for key, value in data.items():
        if value is not None:
            setattr(inventory, key, value)
    await session.commit()
    await session.refresh(inventory)
    return inventory

async def inventory_delete(session: AsyncSession, id: str) -> bool:
    result = await session.execute(select(Inventory).where(Inventory.id == id))
    inventory = result.scalar_one_or_none()
    if not inventory:
        return False
    await session.delete(inventory)
    await session.commit()
    return True

async def inventory_get_all(session: AsyncSession) -> list[Inventory]:
    result = await session.execute(select(Inventory))
    return result.scalars().all()

async def inventory_get_by_model(session:AsyncSession,model_no:str)->Inventory | None:
    result = await session.execute(select(Inventory).where(Inventory.model_no == model_no))
    return result.scalar_one_or_none()