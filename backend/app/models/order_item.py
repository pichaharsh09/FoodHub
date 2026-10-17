from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from ..database.base import Base


from .order import Order
from .food import Food

class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id")
    )

    food_id: Mapped[int] = mapped_column(
        ForeignKey("foods.id")
    )

    quantity: Mapped[int] = mapped_column(
        default=1
    )

    # OrderItem -> Order
    order: Mapped["Order"] = relationship(
        back_populates="order_items"
    )

    # OrderItem -> Food
    food: Mapped["Food"] = relationship(
        back_populates="order_items"
    )