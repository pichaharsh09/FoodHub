from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database.database import get_db
from .. import schemas
from ..services import user_service


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)



@router.post("")
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    return user_service.create_user(
        db,
        user.name,
        user.email,
        user.password
    )


@router.get("")
def get_users(
    db: Session = Depends(get_db)
):
    return user_service.get_users(db)


@router.get("/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return user_service.get_user(db, user_id)

@router.get(
    "/{user_id}/orders",
    response_model=list[schemas.OrderResponse]
)
def get_user_orders(
    user_id: int,
    db: Session = Depends(get_db)
):
    return user_service.get_user_orders(
        db,
        user_id
    )


@router.put("/{user_id}")
def update_user(
    user_id: int,
    user: schemas.UserUpdate,
    db: Session = Depends(get_db)
):
    return user_service.update_user(
        db,
        user_id,
        user.name,
        user.email
    )


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return user_service.delete_user(db, user_id)
