from database.database import obtener_conexion
import json

def create_user(data):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            query = "INSERT INTO user (idwaiter, username, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (data['idwaiter'], data['username'], data['password']))
            conn.commit()
            cursor.close()
            conn.close()
            ret = {"status": "OK", "message": "User created successfully"}
            code = 200
        except Exception as e:
            print(f"Exception while creating user: {e}")
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code

def get_user(user_id):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            query = "SELECT * FROM user WHERE id = %s"
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()
            cursor.close()
            conn.close()
            if user is None:
                ret = {"status": "ERROR", "message": "User not found"}
                code = 404
            else:
                ret = {"status": "OK", "user": user}
                code = 200
        except Exception as e:
            print(f"Exception while fetching user: {e}")
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code

def update_user(user_id, data):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            query = "UPDATE user SET idwaiter = %s, username = %s, password = %s WHERE id = %s"
            cursor.execute(query, (data['idwaiter'], data['username'], data['password'], user_id))
            conn.commit()
            cursor.close()
            conn.close()
            ret = {"status": "OK", "message": "User updated successfully"}
            code = 200
        except Exception as e:
            print(f"Exception while updating user: {e}")
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code

def delete_user(user_id):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            query = "DELETE FROM user WHERE id = %s"
            cursor.execute(query, (user_id,))
            conn.commit()
            cursor.close()
            conn.close()
            ret = {"status": "OK", "message": "User deleted successfully"}
            code = 200
        except Exception as e:
            print(f"Exception while deleting user: {e}")
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code
