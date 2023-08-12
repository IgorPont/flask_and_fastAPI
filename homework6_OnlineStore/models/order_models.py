from pydantic import BaseModel, Field
from homework6_OnlineStore.settings import settings
from datetime import date


class OrderIn(BaseModel):
    user_id: int = Field(..., )
    product_id: int = Field(..., )
    order_date: date = Field(..., format="%Y.%m.%d")
    order_status: str = Field(..., max_length=settings.STRING_MAX_LENGTH)


class Order(OrderIn):
    id: int
