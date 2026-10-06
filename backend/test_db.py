from app.database import SessionLocal
from app.models import  User

db = SessionLocal()

try:
    user = User(
        name="Harsh",
        email="harsh@test.com",
        password="testpassword"
)

    db.add(user)
    db.commit()
    db.refresh(user)

    print(user.id)
    print(user.name)
    print(user.email)

finally:
    db.close()