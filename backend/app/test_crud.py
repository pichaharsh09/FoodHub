from app.database import SessionLocal
from app.crud import create_user, get_users,get_user,update_user, delete_user

db = SessionLocal()

#CREATE
user = create_user(
    db, 
    "Milli", 
    "milli@gmail.com",
    "123456"
)

print("Created:",user.id, user.name, user.email)

#READ ALL
users = get_users(db)

print("All Users:")

for user in users:
    print(user.id, user.name, user.email)

#READ ONE
user = get_user(db,user.id)

print("Single User:",user.id, user.name, user.email)

#UPDATE
user = update_user(
    db,
    user.id,
    "Milli Sheth",
    "millisheth@gmail.com"
)

print("Updated User:",user.id, user.name, user.email)

#DELETE
deleted_user = delete_user(db,user.id)

print("Deleted:",deleted_user.id, deleted_user.name)

db.close()