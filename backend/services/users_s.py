import bcrypt
import jwt
import os
from bson import ObjectId
from config.DataBase import users_collection

JWT_SECRET = os.getenv('JWT_SECRET')

def serialize_user(user):
    user['_id'] = str(user['_id'])
    user.pop('password', None)  # Remove password from the serialized user
    return user

def create_user(data):
    existing_user = users_collection.find_one({'email': data.get('email')})

    if existing_user:
        return None

    hashed_password = bcrypt.hashpw(
        data.get('password').encode('utf-8'),
        bcrypt.gensalt()
    )

    user_data = {
        'name': data.get('name'),
        'email': data.get('email'),
        'password': hashed_password.decode('utf-8'),
        'role': data.get('role', 'user')
    }

    result = users_collection.insert_one(user_data)

    user_data["_id"] = str(result.inserted_id)
    user_data.pop("password", None)

    return user_data

def login_user(data):

    user = users_collection.find_one({"email": data.get("email")})

    if not user:
        return None

    password_valid = bcrypt.checkpw(
        data.get("password").encode("utf-8"),
        user["password"].encode("utf-8")
    )

    if not password_valid:
        return None

    token = jwt.encode({
        "user_id": str(user["_id"]),
        "role": user["role"],
        "email": user["email"]
    }, JWT_SECRET, algorithm="HS256")

    return {
        "token": token,
        "user": serialize_user(user)
}

def get_all_users():
    user = users_collection.find()
    return [serialize_user(user) for user in user]