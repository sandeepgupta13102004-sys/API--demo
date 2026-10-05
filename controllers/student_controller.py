from flask import Flask,jsonify
from models.student_model import(
    get_all_students,
    get_students_by_id,
    create_student,
    update_student,
    delete_student
)

def get_all_students_controller():
    students = get_all_students()
    return jsonify(students)

def get_student_controller(id):
    student = get_students_by_id(id)
    if student:
        return jsonify(student)
    else:
        return jsonify({"message": "Student not found"}), 404

def create_student_controller(data):
    create_student(data)
    student_name = data.get("name", "User")
    return jsonify({"message":f"Hello {student_name}, student created sucessfully!", "data": data}), 201

def update_student_controller(id, data):
    result = update_student(id, data)
    if result:
        return jsonify(result)
    else:
        return jsonify({"message": "Student not found"}), 404

def delete_student_controller(id):
    result = delete_student(id)
    if result:
        return jsonify({"message": "Student deleted successfully"})
    else:
        return jsonify({"message": "Student not found"}), 404



