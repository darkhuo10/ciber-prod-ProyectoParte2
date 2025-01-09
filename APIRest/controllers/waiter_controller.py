from database.database import obtener_conexion
import json
from flask import request
def create_waiter(data):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            query = "INSERT INTO waiter (identification, firstname, lastname1, lastname2, phone, email) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (data['identification'], data['firstname'], data['lastname1'], data.get('lastname2'), data.get('phone'), data.get('email')))
            conn.commit()
            cursor.close()
            conn.close()
            ret = {"status": "OK", "message": "Waiter created successfully"}
            code = 200
        except Exception as e:
            print(f"Exception while creating waiter: {e}")
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code

def get_waiter(waiter_id):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            query = "SELECT * FROM waiter WHERE id = %s"
            cursor.execute(query, (waiter_id,))
            waiter = cursor.fetchone()
            cursor.close()
            conn.close()
            if waiter is None:
                ret = {"status": "ERROR", "message": "Waiter not found"}
                code = 404
            else:
                ret = {"status": "OK", "waiter": waiter}
                code = 200
        except Exception as e:
            print(f"Exception while fetching waiter: {e}")
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code

def update_waiter(waiter_id, data):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            query = "UPDATE waiter SET identification = %s, firstname = %s, lastname1 = %s, lastname2 = %s, phone = %s, email = %s WHERE id = %s"
            cursor.execute(query, (data['identification'], data['firstname'], data['lastname1'], data.get('lastname2'), data.get('phone'), data.get('email'), waiter_id))
            conn.commit()
            cursor.close()
            conn.close()
            ret = {"status": "OK", "message": "Waiter updated successfully"}
            code = 200
        except Exception as e:
            print(f"Exception while updating waiter: {e}")
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code

def delete_waiter(waiter_id):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            query = "DELETE FROM waiter WHERE id = %s"
            cursor.execute(query, (waiter_id,))
            conn.commit()
            cursor.close()
            conn.close()
            ret = {"status": "OK", "message": "Waiter deleted successfully"}
            code = 200
        except Exception as e:
            print(f"Exception while deleting waiter: {e}")
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code
