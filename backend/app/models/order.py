from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String

from ..database.base import Base

from .user import User
from .order_item import OrderItem

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="pending"
    )

    # Order -> User
    user: Mapped["User"] = relationship(
        back_populates="orders"
    )

    # Order -> OrderItems
    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan"
    )