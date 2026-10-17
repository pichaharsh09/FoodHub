from fastapi import HTTPException
from sqlalchemy.orm import Session

from .. import crud
from ..models import Restaurant


def create_food(
    db: Session,
    name: str,
    price: float,
    category: str | None,
    image_url: str | None,
    restaurant_id: int
):
    restaurant = db.get(Restaurant, restaurant_id)

    if restaurant is None:
        raise HTTPException(
            status_code=404,
            detail="Restaurant not found"
        )

    return crud.create_food(
        db=db,
        name=name,
        price=price,
        category=category,
        image_url=image_url,
        restaurant_id=restaurant_id
    )


def get_foods(
    db: Session,
    category: str | None = None,
    search: str | None = None,
    page: int = 1,
    limit: int = 10
):
    return crud.get_foods(
        db,
        category,
        search,
        page,
        limit
    )


def get_food(
    db: Session,
    food_id: int
):
    food = crud.get_food(
        db,
        food_id
    )

    if food is None:
        raise HTTPException(
            status_code=404,
            detail="Food not found"
        )

    return food


def update_food(
    db: Session,
    food_id: int,
    name: str | None,
    price: float | None,
    category: str | None,
    image_url: str | None
):
    food = crud.update_food(
        db,
        food_id,
        name,
        price,
        category,
        image_url
    )

    if food is None:
        raise HTTPException(
            status_code=404,
            detail="Food not found"
        )

    return food


def delete_food(
    db: Session,
    food_id: int
):
    food = crud.delete_food(
        db,
        food_id
    )

    if food is None:
        raise HTTPException(
            status_code=404,
            detail="Food not found"
        )

    return food