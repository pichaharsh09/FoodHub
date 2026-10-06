from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String


from .database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))

    #User -> Orders
    orders: Mapped[list["Order"]] = relationship(
        back_populates="user"
    )

class Restaurant(Base):
    __tablename__ = "restaurants"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(String(255))

    foods: Mapped[list["Food"]] = relationship(
        back_populates="restaurant"
    )

class Food(Base):
    __tablename__ = "foods"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150))
    price: Mapped[float]
    category: Mapped[str] = mapped_column(String(100))
    image_url: Mapped[str | None] = mapped_column(String(500), nullable=True)

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

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    status:Mapped[str] = mapped_column(String(50),default="pending")

    #Order -> User
    user: Mapped["User"] = relationship(
        back_populates="orders"
    )

    #Order -> OrderItems
    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan"
    )

class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    food_id: Mapped[int] = mapped_column(ForeignKey("foods.id"))
    quantity: Mapped[int] = mapped_column(default=1)

    #OrderItem -> Order
    order: Mapped["Order"] = relationship(
        back_populates="order_items"
    )

    #OrderItem -> Food
    food: Mapped["Food"] = relationship(        
        back_populates="order_items"
    )

