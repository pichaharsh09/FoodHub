from fastapi import FastAPI,Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from . import models, crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Food Hub API is running"}

@app.post("/users")
def create_user(
    user: schemas.UserCreate, 
    db: Session = Depends(get_db)
):
    return crud.create_user(
        db, 
        user.name, 
        user.email, 
        user.password
)

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)

@app.put("/users/{user_id}")
def update_user(
    user_id: int, 
    user: schemas.UserUpdate, 
    db: Session = Depends(get_db)
):
    return crud.update_user(
        db, 
        user_id, 
        user.name, 
        user.email
)

@app.delete("/users/{user_id}")
def delete_user(
    user_id: int, 
    db: Session = Depends(get_db)
):
    return crud.delete_user(db, user_id)

@app.post("/restaurants", response_model=schemas.RestaurantResponse)
def create_restaurant(
    restaurant: schemas.RestaurantCreate, 
    db: Session = Depends(get_db)
):
    return crud.create_restaurant(
        db, 
        restaurant.name, 
        restaurant.address
    )

@app.get("/restaurants", response_model=list[schemas.RestaurantResponse])
def get_restaurants(db: Session = Depends(get_db)):
    return crud.get_restaurants(db)

@app.post(
    "/restaurants/{restaurant_id}/foods",
      response_model=schemas.FoodResponse
)
def create_food(
    restaurant_id: int, 
    food: schemas.FoodCreate, 
    db: Session = Depends(get_db)
):
    return crud.create_food(
        db,  
        food.name, 
        food.price,
        restaurant_id,
    )

@app.get(
    "/restaurants/{restaurant_id}/foods", 
    response_model=list[schemas.FoodResponse]
)
def get_foods(
    restaurant_id: int, 
    db: Session = Depends(get_db)
):
    return crud.get_foods_by_restaurant(
    db,
    restaurant_id
)

@app.get(
    "/foods/{food_id}",
    response_model=schemas.FoodResponse
)
def get_food(
    food_id: int, 
    db: Session = Depends(get_db)
):
    return crud.get_food(
        db, 
        food_id
    )

@app.put(
    "/foods/{food_id}",
    response_model=schemas.FoodResponse
)
def update_food(
    food_id: int, 
    food: schemas.FoodUpdate, 
    db: Session = Depends(get_db)
):
    return crud.update_food(
        db, 
        food_id, 
        food.name, 
        food.price
    )

@app.delete(
    "/foods/{food_id}",
    response_model=schemas.FoodResponse
)
def delete_food(
    food_id: int, 
    db: Session = Depends(get_db)
):
    return crud.delete_food(
        db, 
        food_id
    )

@app.get(
    "/foods",
    response_model=list[schemas.FoodResponse]
)
def get_foods(
    category: str | None = None,
    search : str | None = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return crud.get_foods(
        db,
        category,
        search,
        page,
        limit
    )

@app.post(
    "/orders"
)
def create_order(
    order: schemas.OrderCreate, 
    db: Session = Depends(get_db)
):
    return crud.create_order(
        db, 
        order.user_id, 
        order.order_items
    )

@app.get(
    "/orders/{order_id}",
    response_model=schemas.OrderResponse
) 
def get_order(
    order_id: int, 
    db: Session = Depends(get_db)
):
    order = crud.get_orders(
        db,
        order_id
    )

    if order is None:
        raise HTTPException(
            status_code=404, 
            detail="Order not found"
        )

    return order

@app.get(
    "/users/{user_id}/orders",
    response_model=list[schemas.OrderResponse]
)
def get_user_orders(
    user_id: int, 
    db: Session = Depends(get_db)
):
    return crud.get_user_orders(
        db, 
        user_id
    )

@app.delete(
    "/orders/{order_id}",
)
def delete_order(
    order_id: int, 
    db: Session = Depends(get_db)
):
    return crud.delete_order(
        db, 
        order_id
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return {
        "message": "Order deleted successfully"
    }

