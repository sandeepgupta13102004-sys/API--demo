from config import students

def get_all_students():
    return list(students.find({}, {"_id": 0}))

def get_students_by_id(id):
   try:
       numeric_id = int(id)
   except ValueError:
     numeric_id = id
   return students.find_one({"$or":[
      {"id":id},{"id": numeric_id}]
   },{"_id":0})

def create_student(data):
 return students.insert_one({ 
    "id": data.get("id"),
    "name": data["name"],
    "age": data["age"],
    "email": data["email"]
 })


def update_student(id, data):
 return students.update_one({"id": id}, {"$set": {
    "name": data["name"],
    "age": data["age"],
    "email": data["email"]
    }})


def delete_student(id):
 return students.delete_one({"id": id})
