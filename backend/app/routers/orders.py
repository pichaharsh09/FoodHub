from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database.database import get_db
from .. import schemas
from ..services import order_service


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("")
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db)
):
    return order_service.create_order(
        db,
        order.user_id,
        order.order_items
    )


@router.get(
    "/{order_id}",
    response_model=schemas.OrderResponse
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    return order_service.get_order(
        db,
        order_id
    )


@router.delete("/{order_id}")
def delete_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    result = order_service.delete_order(
        db,
        order_id
    )

    return {
        "message": "Order deleted successfully"
    }