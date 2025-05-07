from flask import request, session, jsonify
import json
import decimal
from __main__ import app
from routes.waiter_routes import json_to_waiter
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
    user, code = user_controller.get_user_by_id(user_id)
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
def register_user():
    content_type = request.headers.get('Content-Type')

    if content_type == 'application/json':
        try:
            # Extract the request body
            data = request.json

            # Separate user data and waiter data from the request
            user_json = {
                'username': data.get('username'),
                'password': data.get('password')
            }
            waiter_json = {
                'identification': data.get('identification'),
                'firstname': data.get('firstname'),
                'lastname1': data.get('lastname1'),
                'lastname2': data.get('lastname2'),
                'phone': data.get('phone'),
                'email': data.get('email')
            }

            # Ensure both user and waiter data are provided
            if not user_json or not waiter_json:
                return json.dumps({"status": "error", "message": "Missing user or waiter data"}), 400

            # Step 1: Register the waiter (create waiter)
            ret, code = waiter_controller.create_waiter(json_to_waiter(waiter_json))
            if code != 200:
                return json.dumps({"status": "error", "message": "Waiter creation failed", "details": ret}), code

            # Step 2: Get the ID of the created waiter
            id_waiter = ret.get('id')
            if not id_waiter:
                return json.dumps({"status": "error", "message": "Waiter creation did not return an ID"}), 500

            # Log the ID to make sure it's retrieved correctly
            app.logger.debug(f"Created waiter ID: {id_waiter}")

            # Step 3: Register the user with the waiter ID
            username = user_json.get('username')
            password = user_json.get('password')
            user_ret, user_code = user_controller.register_user(id_waiter, username, password)

            # Log user registration response for debugging
            app.logger.debug(f"User registration response: {user_ret}, status code: {user_code}")

            if user_code != 200:
                return json.dumps({"status": "error", "message": "User registration failed", "details": user_ret}), user_code

            # Step 4: Return success message
            return json.dumps({"status": "OK", "message": "Usuario registrado con éxito"}), 200

        except Exception as e:
            # Log the unexpected error
            app.logger.error(f"Unexpected error during registration: {str(e)}")
            return json.dumps({"status": "error", "message": str(e)}), 500
    else:
        # Bad request, JSON expected
        return json.dumps({"status": "error", "message": "Bad request, JSON expected"}), 400

