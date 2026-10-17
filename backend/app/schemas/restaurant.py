from pydantic import BaseModel


class RestaurantCreate(BaseModel):
    name: str
    address: str


class RestaurantResponse(BaseModel):
    id: int
    name: str
    address: str

    model_config = {
        "from_attributes": True
    }