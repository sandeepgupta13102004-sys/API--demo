from flask import  jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity
from models.user_model import (
    create_user,
    get_user_by_email,
    check_user_password,
    update_user 
)

def login_user_controller(data):
    print("DATA:", data)
    print("DATA TYPE:", type(data))
    if not data:
        return jsonify({"message": "Request body is required"}), 400

    if "email" not in data:
        return jsonify({"message": "Email is required"}), 400

    if "password" not in data:
        return jsonify({"message": "Password is required"}), 400

    user = get_user_by_email(data["email"])
    if not user:
        return jsonify({"message": "Invalid email or password"}), 401

    if not check_user_password(user, data["password"]):
        return jsonify({"message": "Invalid email or password"}), 401

    access_token = create_access_token(identity=str(user["_id"]))
    return jsonify({"message": "Login successful", "access_token": access_token,
    "user": {
    "id": str(user["_id"]),
    "name": user["name"], 
    "email": user["email"]}}), 200

def register_user_controller(data):
    if not data:
        return jsonify({"message": "Request body is required"}), 400
    
    if "name" not in data or "email" not in data or "password" not in data:
        return jsonify({"message": "Name, email, and password are required"}), 400

    new_user = create_user(data)
    return jsonify({"message": "User registered successfully", "user": new_user}), 201

def login_user_controller(data):
    print("DATA:", data)
    print("DATA TYPE:", type(data))
    if not data:
        return jsonify({"message": "Request body is required"}), 400
    
    if "email" not in data:
        return jsonify({"message": "Email is required"}), 400

    if "password" not in data:
        return jsonify({"message": "Password is required"}), 400

    user = get_user_by_email(data["email"])
    if not user:
        return jsonify({"message": "Invalid email or password"}), 401

    if not check_user_password(user, data["password"]):
        return jsonify({"message": "Invalid email or password"}), 401

    print("Login successful for user:", user["_id"])
    return jsonify({"message": "Login successful",
                "access_token": create_access_token(identity=str(user["_id"])),
                "user": {
                    "id": str(user["_id"]), 
                    "name": user["name"],
                    "email": user["email"]}}), 200

def update_user_controller(user_id):
    current_user_id = get_jwt_identity()
    print("Logged in user:", current_user_id)
    data = request.get_json()

    if not data:
        return jsonify({"message": "Request body is required"}), 400
    user = update_user(user_id, data)

    if user is None:
        return jsonify({"message": "User not found"}), 404
    return jsonify({"message": "Profile updated successfully",
        "user": {
            "id": user["_id"],
            "name": user["name"],
            "email": user["email"]
            }
        }), 200

   