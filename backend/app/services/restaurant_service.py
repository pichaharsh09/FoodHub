from fastapi import HTTPException
from sqlalchemy.orm import Session

from .. import crud
from ..repositories import restaurant_repository


def create_restaurant(
    db: Session,
    name: str,
    address: str
):
    return restaurant_repository.create_restaurant(
        db,
        name,
        address
    )


def get_restaurants(db: Session):
    return restaurant_repository.get_restaurants(db)


def get_restaurant(
    db: Session,
    restaurant_id: int
):
    restaurant = restaurant_repository.get_restaurant(
        db,
        restaurant_id
    )

    if restaurant is None:
        raise HTTPException(
            status_code=404,
            detail="Restaurant not found"
        )

    return restaurant


def create_food(
    db: Session,
    restaurant_id: int,
    name: str,
    price: float,
    category: str | None
):
    return crud.create_food(
        db=db,
        name=name,
        price=price,
        category=category,
        image_url=None,
        restaurant_id=restaurant_id
    )

def update_restaurant(
    db: Session,
    restaurant_id: int,
    name: str,
    address: str
):
    restaurant = restaurant_repository.get_restaurant(
        db,
        restaurant_id
    )

    if restaurant is None:
        raise HTTPException(
            status_code=404,
            detail="Restaurant not found"
        )

    return restaurant_repository.update_restaurant(
        db,
        restaurant,
        name,
        address
    )

def delete_restaurant(
    db: Session,
    restaurant_id: int
):
    restaurant = restaurant_repository.get_restaurant(
        db,
        restaurant_id
    )

    if restaurant is None:
        raise HTTPException(
            status_code=404,
            detail="Restaurant not found"
        )

    restaurant_repository.delete_restaurant(
        db,
        restaurant
    )

    return {
        "message": "Restaurant deleted successfully"
    }

def get_restaurant_foods(
    db: Session,
    restaurant_id: int
):
    return crud.get_restaurant_foods(
        db,
        restaurant_id
    )


def get_foods_by_restaurant(
    db: Session,
    restaurant_id: int
):
    return crud.get_foods_by_restaurant(
        db,
        restaurant_id
    )