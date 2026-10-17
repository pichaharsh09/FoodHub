from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import User, Restaurant, Food, Order, OrderItem
from .exceptions import (
    UserNotFoundError,
    RestaurantNotFoundError,
    FoodNotFoundError,
    OrderNotFoundError,
)

def create_user(db: Session, name: str, email: str, password: str):
    user = User(
        name=name,
        email=email,
        password=password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_users(db: Session):
    stmt = select(User)

    result = db.execute(stmt)

    return result.scalars().all()

def get_user(db: Session, user_id: int):
    stmt = select(User).where(User.id == user_id)
    result = db.execute(stmt)
    user = result.scalar_one_or_none()

    if user is None:
        raise UserNotFoundError("User not found")

    return user

def update_user(
        db: Session,
        user_id: int,
        name: str,
        email: str
):
    user = get_user(db, user_id)



    user.name = name
    user.email = email

    db.commit()
    db.refresh(user)

    return user

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)



    db.delete(user)
    db.commit()

    return user



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



def get_foods(
        db: Session,
        category: str | None = None,
        search: str | None = None,
        page: int = 1,
        limit: int = 10
):
    stmt = select(Food)

    if category:
        stmt = stmt.where(
            Food.category == category
        )

    if search:
        stmt = stmt.where(
            Food.name.ilike(f"%{search}%")
        )

    stmt = stmt.order_by(Food.id.desc())

    offset = (page - 1) * limit
    stmt = stmt.offset(offset).limit(limit)

    result = db.execute(stmt)

    return result.scalars().all()

def get_foods_by_restaurant(
        db: Session,
        restaurant_id: int
):
    stmt = select(Food).where(
        Food.restaurant_id == restaurant_id
    )

    result = db.execute(stmt)

    return result.scalars().all()

def get_food(db: Session, food_id: int):
    stmt = select(Food).where(Food.id == food_id)
    result = db.execute(stmt)
    food = result.scalar_one_or_none()

    if food is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
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
    food = get_food(db, food_id)



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

def delete_food(db: Session, food_id: int):
    food = get_food(db, food_id)



    db.delete(food)
    db.commit()

    return food

def create_order(
        db: Session,
        user_id: int,
        items
):
    order = Order(
        user_id=user_id
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    for item in items:
        order_item = OrderItem(
            order_id=order.id,
            food_id=item.food_id,
            quantity=item.quantity
        )
        db.add(order_item)

    db.commit()
    db.refresh(order)

    return order


def get_orders(db: Session, order_id: int):
    stmt = select(Order).where(Order.id == order_id)
    result = db.execute(stmt)
    order = result.scalar_one_or_none()

    if order is None:
        raise OrderNotFoundError("Order not found")
    return order


def get_user_orders(db: Session, user_id: int):
    stmt = select(Order).where(Order.user_id == user_id)

    result = db.execute(stmt)

    return result.scalars().all()

def delete_order(db: Session, order_id: int):
    order = get_orders(db, order_id)



    db.delete(order)
    db.commit()

    return True
