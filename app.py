from flask import Flask, render_template
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes.student_routes import student_bp
from routes.user_routes import user_bp

app = Flask (__name__)
CORS(app, resources={
    r"/*":{
        "origins":"http://127.0.0.1:5500",
        "methods":["GET","POST","PUT","DELETE","OPTIONS"],
        "allow_headers":["Content-Type", "Authorization"]
    }
})
app.config["JWT_SECRET_KEY"] = "my-secret-key"
jwt = JWTManager(app)
app.register_blueprint(student_bp)
app.register_blueprint(user_bp)


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run( port=5001,debug=True)