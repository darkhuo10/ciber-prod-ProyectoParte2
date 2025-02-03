from flask import request, session, jsonify
import json
import decimal
from __main__ import app
from controllers import user_controller
from models.models import User


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

# routes for /me, /login, /register
'''
Check with postman
@app.route("/me",methods=["GET"])
@app.route("/login",methods=["POST"])
@app.route("/register",methods=["POST"])'''

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

@app.route("/register", methods=["POST"])
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
    return json.dumps(ret), code
