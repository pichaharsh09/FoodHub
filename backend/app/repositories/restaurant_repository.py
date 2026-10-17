from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models import Restaurant


def create_restaurant(
    db: Session,
    name: str,
    address: str
):
    restaurant = Restaurant(
        name=name,
        address=address
    )

    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)

    return restaurant


def get_restaurants(db: Session):
    stmt = select(Restaurant)

    result = db.execute(stmt)

    return result.scalars().all()

def get_restaurant(
    db: Session,
    restaurant_id: int
):
    stmt = select(Restaurant).where(
        Restaurant.id == restaurant_id
    )

    result = db.execute(stmt)

    return result.scalar_one_or_none()

def update_restaurant(
    db: Session,
    restaurant: Restaurant,
    name: str,
    address: str
):
    restaurant.name = name
    restaurant.address = address

    db.commit()
    db.refresh(restaurant)

    return restaurant

def delete_restaurant(
    db: Session,
    restaurant: Restaurant
):
    db.delete(restaurant)
    db.commit()

    return restaurant
