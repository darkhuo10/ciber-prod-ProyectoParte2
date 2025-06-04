from __future__ import print_function
from __main__ import app
from flask import request, make_response
import json
from common.functions import Encoder, sanitize_input, delete_session
from controllers import user_controller

@app.route("/login",methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        login_json = request.json
        if "username" in login_json and "password" in login_json:
            username = sanitize_input(login_json['username'])
            password = sanitize_input(login_json['password'])
            if isinstance(username, str) and isinstance(password, str) and len(username) < 50 and len(password) < 50:
                respuesta,code= user_controller.login_usuario(username,password)
            else:
                respuesta={"status":"Bad parameters"}
                code=401
        else:
            respuesta={"status":"Bad request"}
            code=401
    else:
        respuesta={"status":"Bad request"}
        code=401
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response

@app.route("/register",methods=['POST'])
def register():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        login_json = request.json
        if "username" in login_json and "password" in login_json and "role" in login_json and "email" in login_json:
            username = sanitize_input(login_json['username'])
            password = sanitize_input(login_json['password'])
            role = sanitize_input(login_json['role'])
            email = sanitize_input(login_json['email'])
            if isinstance(username, str) and isinstance(password, str) and isinstance(role, str) and len(username) < 50 and len(password) < 50:
                respuesta,code= user_controller.register_user(username,password,role,email)
            else:
                respuesta={"status":"Bad parameters"}
                code=401
        else:
            respuesta={"status":"Bad request"}
            code=401
    else:
        respuesta={"status":"Bad request"}
        code=401
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response


@app.route("/logout",methods=['GET'])
def logout():
    try:
        delete_session()
        ret={"status":"OK"}
        code=200
    except:
        ret={"status":"ERROR"}
        code=500
    response=make_response(json.dumps(ret),code)
    return response
