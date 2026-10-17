from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from ..database.database import get_db
from .. import schemas
from ..services import food_service


router = APIRouter(
    prefix="/foods",
    tags=["Foods"]
)


@router.post(
    "",
    response_model=schemas.FoodResponse
)
def create_food(
    food: schemas.FoodCreate,
    db: Session = Depends(get_db)
):
    return food_service.create_food(
        db=db,
        name=food.name,
        price=food.price,
        category=food.category,
        image_url=None,
        restaurant_id=food.restaurant_id
    )


@router.get(
    "",
    response_model=list[schemas.FoodResponse]
)
def get_foods(
    category: str | None = Query(default=None),
    search: str | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return food_service.get_foods(
        db=db,
        category=category,
        search=search,
        page=page,
        limit=limit
    )


@router.get(
    "/{food_id}",
    response_model=schemas.FoodResponse
)
def get_food(
    food_id: int,
    db: Session = Depends(get_db)
):
    return food_service.get_food(
        db=db,
        food_id=food_id
    )


@router.put(
    "/{food_id}",
    response_model=schemas.FoodResponse
)
def update_food(
    food_id: int,
    food: schemas.FoodUpdate,
    db: Session = Depends(get_db)
):

    print(food)
    print(food.model_dump(exclude_unset=True))

    return food_service.update_food(
        db=db,
        food_id=food_id,
        name=food.name,
        price=food.price,
        category=food.category,
        image_url=food.image_url
    )


@router.delete(
    "/{food_id}",
    response_model=schemas.FoodResponse
)
def delete_food(
    food_id: int,
    db: Session = Depends(get_db)
):
    return food_service.delete_food(
        db=db,
        food_id=food_id
    )