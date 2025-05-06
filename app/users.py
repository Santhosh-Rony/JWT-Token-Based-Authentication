from .auth import get_password_hash
from .schemas import UserInDB

users_db = {
    "admin": UserInDB(
        username="admin",
        hashed_password=get_password_hash("adminpass"),
        role="admin"
    ),
    "user": UserInDB(
        username="user",
        hashed_password=get_password_hash("userpass"),
        role="user"
    )
}

def get_user(username: str):
    return users_db.get(username)
