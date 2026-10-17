from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String

from ..database.base import Base

from .restaurant import Restaurant
from .order_item import OrderItem

class Food(Base):
    __tablename__ = "foods"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150))
    price: Mapped[float] = mapped_column()
    category: Mapped[str] = mapped_column(String(100))
    image_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    restaurant_id: Mapped[int] = mapped_column(
        ForeignKey("restaurants.id")
    )

    restaurant: Mapped["Restaurant"] = relationship(
        back_populates="foods"
    )

    # Food -> OrderItems
    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="food"
    )