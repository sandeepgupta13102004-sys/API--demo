from flask import Blueprint,request,jsonify
from controllers.student_controller import (
     get_all_students_controller,
    get_student_controller,
    create_student_controller,
    update_student_controller,
    delete_student_controller
)

student_bp = Blueprint('student', __name__)

@student_bp.route("/students", methods=["GET", "OPTIONS"])

def get_all_students():
    return get_all_students_controller() 

@student_bp.route("/students/<student_id>", methods=["GET"])
def get_student(student_id):
    return get_student_controller(student_id)


@student_bp.route("/students",methods=["POST"])
def create_student():
    data = request.get_json()
    return create_student_controller( data)


@student_bp.route("/students/<int:student_id>",methods=["PUT"])
def update_student(student_id):
    data = request.get_json()
    return update_student_controller(student_id,data)

@student_bp.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    return delete_student_controller(student_id)
