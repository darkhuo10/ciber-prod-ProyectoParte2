from flask import request, session, jsonify
import json
import decimal
from __main__ import app
from controllers import waiter_controller
from models.models import Waiter

def json_to_waiter(waiter_json):
    waiter = Waiter(
        waiter_json.get('identification'),
        waiter_json.get('firstname'),
        waiter_json.get('lastname1'),
        waiter_json.get('lastname2'),
        waiter_json.get('phone'),
        waiter_json.get('email'),
        waiter_json.get('username'),
        #waiter_json.get('isadmin'),
        waiter_json.get('password')
        
    )
    return waiter

@app.route("/waiters", methods=["GET"])
def get_all_waiters():
    waiters, code = waiter_controller.get_all_waiters()
    return jsonify(waiters), code

@app.route("/waiter/<id>", methods=["GET"])
def get_waiter_by_id(id):
    waiter, code = waiter_controller.get_waiter_by_id(id)
    return jsonify(waiter), code


@app.route("/waiter/create",methods=["POST"])
def create_waiter():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        waiter_json = request.json
        ret,code=waiter_controller.create_waiter(json_to_waiter(waiter_json))
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/waiter/delete/<id>", methods=["DELETE"])
def delete_waiter(id):
    ret,code=waiter_controller.delete_waiter(id)
    return json.dumps(ret), code

@app.route("/waiter/update", methods=["PUT"])
def update_waiter():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        waiter_json = request.json
        ret,code=waiter_controller.update_waiter(json_to_waiter(waiter_json))
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/login", methods=["POST"])
def login():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        user_json = request.json
        username = user_json.get("username")
        password = user_json.get("password")
        
        ret, code = waiter_controller.login_user(username, password)
        
        if ret.get("status") == "OK":
            session["user_id"] = ret["user"]["id"]
        
    else:
        ret = {"status": "Bad request"}
        code = 401
    
    return json.dumps(ret), code