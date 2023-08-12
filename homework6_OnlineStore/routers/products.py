from fastapi import APIRouter, Query, HTTPException
from homework6_OnlineStore.models.product_models import ProductIn, Product
from homework6_OnlineStore.database import products, db

router = APIRouter()


@router.get("/products", response_model=list[Product])
async def get_products(
        skip: int = Query(default=None, title="Skip count", ge=0),
        count: int = Query(default=None, title="Get count", ge=0),
):
    query = products.select().offset(skip).limit(count)
    return await db.fetch_all(query=query)


@router.get("/products/{product_id}", response_model=Product)
async def get_product_by_id(product_id: int):
    query = products.select().where(products.c.id == product_id)
    data = await db.fetch_one(query=query)
    if not data:
        raise HTTPException(status_code=404, detail="Product not found")
    return data


@router.post("/products", response_model=Product)
async def create_product(product: ProductIn):
    query = products.insert().values(**product.model_dump())
    product_id = await db.execute(query=query)
    return Product(**product.model_dump(), id=product_id)


@router.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**product.model_dump())
    res = await db.execute(query=query)
    if res > 0:
        return Product(**product.model_dump(), id=product_id)
    raise HTTPException(status_code=404, detail="Product not found")


@router.delete("/products/{product_id}", response_model=dict)
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    res = await db.execute(query=query)
    if res > 0:
        return {"message": "Product was successfully deleted"}
    raise HTTPException(status_code=404, detail="Product not found")
