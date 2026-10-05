from unittest import result
from config import users
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

def create_user(data):
    user = {
        "name": data.get("name"),
        "email": data.get("email"),
        "password": generate_password_hash(data.get("password"))
    }
    users.insert_one(user)
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"]
    }
def get_user_by_email(email):
    return users.find_one({"email": email})

def check_user_password(user,password):
    return check_password_hash(user["password"], password)

def update_user(user_id, data):
    updated_data = {}

    if "name" in data:
        updated_data["name"] = data["name"]

    if "email" in data:
        updated_data["email"] = data["email"]

    if "password" in data:
        updated_data["password"] = generate_password_hash(data["password"])


    if not updated_data:
        return None
        result = users.update_one
        ({"_id": ObjectId(user_id)},
        {"$set": updated_data}
     )
    if result.matched_count == 0:
        return None
                  
    updated_user = users.find_one({"_id": ObjectId(user_id)})

    return updated_user
    