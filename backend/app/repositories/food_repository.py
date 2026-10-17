from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models import Food


def create_food(
    db: Session,
    name: str,
    price: float,
    category: str | None,
    image_url: str | None,
    restaurant_id: int
):
    food = Food(
        name=name,
        price=price,
        category=category,
        image_url=image_url,
        restaurant_id=restaurant_id
    )

    db.add(food)
    db.commit()
    db.refresh(food)

    return food


def get_foods(db: Session):
    stmt = select(Food)

    result = db.execute(stmt)

    return result.scalars().all()


def get_food(
    db: Session,
    food_id: int
):
    stmt = select(Food).where(
        Food.id == food_id
    )

    result = db.execute(stmt)

    return result.scalar_one_or_none()


def update_food(
    db: Session,
    food: Food,
    name: str | None,
    price: float | None,
    category: str | None,
    image_url: str | None
):
    if name is not None:
        food.name = name

    if price is not None:
        food.price = price

    if category is not None:
        food.category = category

    if image_url is not None:
        food.image_url = image_url

    db.commit()
    db.refresh(food)

    return food


def delete_food(
    db: Session,
    food: Food
):
    db.delete(food)
    db.commit()

    return food