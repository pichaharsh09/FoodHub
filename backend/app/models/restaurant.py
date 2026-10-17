from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from ..database.base import Base

from .food import Food

class Restaurant(Base):
    __tablename__ = "restaurants"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(String(255))

    foods: Mapped[list["Food"]] = relationship(
        back_populates="restaurant"
    )