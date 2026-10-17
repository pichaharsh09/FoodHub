from pydantic import BaseModel

from .food import FoodResponse


class OrderItemCreate(BaseModel):
    food_id: int
    quantity: int = 1


class OrderCreate(BaseModel):
    user_id: int
    order_items: list[OrderItemCreate]


class OrderItemResponse(BaseModel):
    id: int
    food_id: int
    quantity: int
    food: FoodResponse

    model_config = {
        "from_attributes": True
    }


class OrderResponse(BaseModel):
    id: int
    user_id: int
    status: str
    order_items: list[OrderItemResponse]

    model_config = {
        "from_attributes": True
    }