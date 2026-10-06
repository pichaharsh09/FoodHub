from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str
    email:str
    password:str

class UserUpdate(BaseModel):
    name:str
    email:str

class RestaurantCreate(BaseModel):
    name:str
    address:str

class RestaurantResponse(BaseModel):
    id:int
    name:str
    address:str

    model_config = {
        "from_attributes": True
    }

class FoodCreate(BaseModel):
    name:str
    price:float

class FoodResponse(BaseModel):
    id: int
    name: str
    price: float
    category: str
    restaurant_id: int

    model_config = {
        "from_attributes": True
    }

class FoodUpdate(BaseModel):
    name:str
    price:float


class OrderItemCreate(BaseModel):
    food_id:int
    quantity:int = 1

class OrderCreate(BaseModel):
    user_id:int
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