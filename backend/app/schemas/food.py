from pydantic import BaseModel


class FoodCreate(BaseModel):
    name: str
    price: float
    category: str | None = None
    restaurant_id: int


class FoodUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    category: str | None = None
    image_url: str | None = None


class FoodResponse(BaseModel):
    id: int
    name: str
    price: float
    category: str
    image_url: str | None
    restaurant_id: int

    model_config = {
        "from_attributes": True
    }