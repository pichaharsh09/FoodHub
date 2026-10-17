from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from ..database.base import Base

from .order import Order

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))

    # User -> Orders
    orders: Mapped[list["Order"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )