from fastapi import APIRouter, HTTPException
from typing import Union
from models.item import Item


router = APIRouter(
    prefix="/api/v1/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    """
    displays the item api
    """
    return {"item_id": item_id, "q": q}


@router.put("/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name}
