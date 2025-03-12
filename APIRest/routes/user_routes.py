from flask import request, session, jsonify
import json
import decimal
from __main__ import app
from controllers import user_controller, waiter_controller
from models.models import User, Waiter


def json_to_user(user_json):
    user = User(
        user_json.get('id_waiter'),
        user_json.get('username'),
        user_json.get('password'),
        user_json.get('is_admin'))
    return user

@app.route("/users",methods=["GET"])
def get_all_users():
    users,code= user_controller.get_all_users()
    return jsonify(users), code
@app.route("/user/<id>",methods=["GET"])
def get_user_by_id(id):
    user,code = user_controller.get_user_by_id(id)
    return jsonify(user), code
@app.route("/user/create",methods=["POST"])
def create_user():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        user_json = request.json
        ret,code=user_controller.create_user(json_to_user(user_json))
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/user/delete/<id>", methods=["DELETE"])
def delete_user(id):
    ret,code=user_controller.delete_user(id)
    return json.dumps(ret), code

@app.route("/user", methods=["PUT"])
def update_user():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        user_json = request.json
        ret,code=user_controller.create_user(json_to_user(user_json))
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/me", methods=["GET"])
def get_me():
    user_id = session.get("user_id")
    user, code = user_controller.get_user_by_id(int(user_id))
    return jsonify(user), code

@app.route("/login", methods=["POST"])
def login():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        user_json = request.json
        username = user_json.get("username")
        password = user_json.get("password")
        
        ret, code = user_controller.login_user(username, password)
        
        if ret.get("status") == "OK":
            session["user_id"] = ret["user"]["id"]
        
    else:
        ret = {"status": "Bad request"}
        code = 401
    
    return json.dumps(ret), code

'''@app.route("/register", methods=["POST"])
def register():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        user_json = request.json
        id_waiter = user_json.get("id_waiter")
        username = user_json.get("username")
        password = user_json.get("password")
        ret, code = user_controller.register_user(id_waiter, username, password)
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code'''

@app.route("/register", methods=["POST"])
def register():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        user_json = request.json
        id_waiter = user_json.get("id_waiter")
        username = user_json.get("username")
        password = user_json.get("password")
        identification = user_json.get("identification")
        firstname = user_json.get("firstname")
        lastname1 = user_json.get("lastname1")
        lastname2 = user_json.get("lastname2")
        phone = user_json.get("phone")
        email = user_json.get("email")

        # First register the user
        ret, code = user_controller.register_user(id_waiter, username, password)
        
        if ret["status"] == "OK":
            # If user registration is successful, create the waiter
            waiter = Waiter(
                identification=identification,
                firstname=firstname,
                lastname1=lastname1,
                lastname2=lastname2,
                phone=phone,
                email=email
            )
            waiter_ret = waiter_controller.create_waiter(waiter)

            if waiter_ret["status"] == "OK":
                return json.dumps({"status": "OK"}), 200
            else:
                return json.dumps({"status": "Failure", "message": "Error creating waiter"}), 500
        else:
            return json.dumps(ret), code
    else:
        return json.dumps({"status": "Bad request"}), 401