from fastapi import HTTPException
from sqlalchemy.orm import Session

from .. import crud


def create_order(
    db: Session,
    user_id: int,
    order_items: list
):
    return crud.create_order(
        db,
        user_id,
        order_items
    )


def get_order(
    db: Session,
    order_id: int
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


def delete_order(
    db: Session,
    order_id: int
):
    result = crud.delete_order(
        db,
        order_id
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return result