from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database.database import get_db
from .. import schemas
from ..services import restaurant_service


router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurants"]
)


# =========================
# RESTAURANT ENDPOINTS
# =========================

@router.post(
    "",
    response_model=schemas.RestaurantResponse
)
def create_restaurant(
    restaurant: schemas.RestaurantCreate,
    db: Session = Depends(get_db)
):
    return restaurant_service.create_restaurant(
        db,
        restaurant.name,
        restaurant.address
    )


@router.get(
    "",
    response_model=list[schemas.RestaurantResponse]
)
def get_restaurants(
    db: Session = Depends(get_db)
):
    return restaurant_service.get_restaurants(db)


@router.get(
    "/{restaurant_id}",
    response_model=schemas.RestaurantResponse
)
def get_restaurant(
    restaurant_id: int,
    db: Session = Depends(get_db)
):
    return restaurant_service.get_restaurant(
        db,
        restaurant_id
    )

@router.put(
    "/{restaurant_id}",
    response_model=schemas.RestaurantResponse
)
def update_restaurant(
    restaurant_id: int,
    restaurant: schemas.RestaurantCreate,
    db: Session = Depends(get_db)
):
    return restaurant_service.update_restaurant(
        db,
        restaurant_id,
        restaurant.name,
        restaurant.address
    )

@router.delete("/{restaurant_id}")
def delete_restaurant(
    restaurant_id: int,
    db: Session = Depends(get_db)
):
    return restaurant_service.delete_restaurant(
        db,
        restaurant_id
    )


# =========================
# FOOD ENDPOINTS
# =========================

@router.post(
    "/{restaurant_id}/foods",
    response_model=schemas.FoodResponse
)
def create_food(
    restaurant_id: int,
    food: schemas.FoodCreate,
    db: Session = Depends(get_db)
):
    return restaurant_service.create_food(
        db,
        restaurant_id,
        food.name,
        food.price,
        food.category
    )


@router.get(
    "/{restaurant_id}/foods",
    response_model=list[schemas.FoodResponse]
)
def get_foods_by_restaurant(
    restaurant_id: int,
    db: Session = Depends(get_db)
):
    return restaurant_service.get_foods_by_restaurant(
        db,
        restaurant_id
    )