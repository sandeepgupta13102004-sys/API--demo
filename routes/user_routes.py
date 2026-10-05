from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from controllers.user_controller import (
    register_user_controller,
    login_user_controller,
    update_user_controller
)

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    return register_user_controller(data)

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    return login_user_controller(data)

@user_bp.route("/users/<user_id>", methods=["PUT"])
@jwt_required()
def update_profile(user_id):
    data = request.get_json()
    return update_user_controller(user_id, data)