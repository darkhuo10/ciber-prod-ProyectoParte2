from flask import request, session
import json
import decimal
from __main__ import app
from controllers import user_controller

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

@app.route("/users",methods=["GET"])
def get_all_users():
    users,code= user_controller.get_all_users()
    return json.dumps(users, cls = Encoder),code

@app.route("/user/<id>",methods=["GET"])
def get_user_by_id(id):
    user,code = user_controller.get_user_by_id(id)
    return json.dumps(user, cls = Encoder),code

@app.route("/user/create",methods=["POST"])
def create_user():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        user_json = request.json
        ret,code=user_controller.create_user(user_json) #Check if need to pass to object again
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
        ret,code=user_controller.update_user(user_json)
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

# routes for /me, /login, /register
'''
@app.route("/me",methods=["GET"])
@app.route("/login",methods=["POST"])
@app.route("/register",methods=["POST"])'''

