from fastapi import APIRouter, Query, HTTPException
from homework6_OnlineStore.models.order_models import OrderIn, Order
from homework6_OnlineStore.database import orders, db

router = APIRouter()


@router.get("/orders", response_model=list[Order])
async def get_orders(
        skip: int = Query(default=None, title="Skip count", ge=0),
        count: int = Query(default=None, title="Get count", ge=0),
):
    query = orders.select().offset(skip).limit(count)
    return await db.fetch_all(query=query)


@router.get("/orders/{order_id}", response_model=Order)
async def get_order_by_id(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    data = await db.fetch_one(query=query)
    if not data:
        raise HTTPException(status_code=404, detail="Order not found")
    return data


@router.post("/orders", response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(**order.model_dump())
    order_id = await db.execute(query=query)
    return Order(**order.model_dump(), id=order_id)


@router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**order.model_dump())
    res = await db.execute(query=query)
    if res > 0:
        return Order(**order.model_dump(), id=order_id)
    raise HTTPException(status_code=404, detail="Order not found")


@router.delete("/orders/{order_id}", response_model=dict)
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    res = await db.execute(query=query)
    if res > 0:
        return {"message": "Order was successfully deleted"}
    raise HTTPException(status_code=404, detail="Order not found")
