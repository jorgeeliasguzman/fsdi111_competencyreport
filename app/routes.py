from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLACHEMY_DATABASE_URI"] = "sqlite://mydb.db"
db = SQLAlchemy(app)


from app.database import User

@app.route("/")
def index():
    username = "Juan"
    return render_template("index.html", name=username)

@app.route("/greet/<username>")
def greeting(username):
    return render_template("index.html", name=username)

@app.route("/users/<int:uid>/profiles")
def get_profile(uid):
    user = User.query.filter_by(id=uid).first()
    return render_template("user_profile.html", user=user)

@app.route("/users/profiles")
def list_users():
    list_of_users = User.query.filter_by(id=uid).first()
    return render_template("user_profile.html", user=user)



@app.route("/users")
def get_all_users():
    out = {
        "ok": True,
        "message": "Success"
    }
    out["body"] = scan()
    return out


@app.route("/users", methods={"POST"})
def create_user():
    out = {
        "ok": True,
        "message": "Success"
    }
    user_data = request.json
    out["new_id"] = insert(
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies"),
    )
    return out, 201


@app.route("/users/<int:uid>", methods={"DELETE"})
def delete_user(uid):
    out = {
        "ok": True,
        "message": "Success"
    }
    deactivate_user(uid)
    return out, 200


@app.route("/users/<int:uid>", methods={"GET"})
def get_single_user(uid):
    out = {
        "ok": True,
        "message": "Success"
    }
    out["body"] = select(uid)
    return out

@app.route('/agent')
def agent():
    user_agent = request

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404