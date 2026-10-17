from sqlalchemy.orm import Session

from .. import crud


def create_user(
    db: Session,
    name: str,
    email: str,
    password: str
):
    return crud.create_user(
        db,
        name,
        email,
        password
    )


def get_users(db: Session):
    return crud.get_users(db)


def get_user(db: Session, user_id: int):
    return crud.get_user(db, user_id)


def update_user(
    db: Session,
    user_id: int,
    name: str,
    email: str
):
    return crud.update_user(
        db,
        user_id,
        name,
        email
    )


def delete_user(db: Session, user_id: int):
    return crud.delete_user(db, user_id)


def get_user_orders(db: Session, user_id: int):
    return crud.get_user_orders(db, user_id)