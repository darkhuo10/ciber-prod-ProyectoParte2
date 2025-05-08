from __future__ import print_function
from database import database
from models.models import User
import sys

def user_to_json(row):
    return {
        "id": row[0],
        "id_waiter": row[1],
        "username": row[2],
        "password": row[3],
        "is_admin": row[4]
    }

def login_user(username: str, password: str):
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, id_waiter, username FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
        conexion.close()
        if user:
            return {"status": "OK", "user": user_to_json(user)}, 200
        else:
            return {"status": "ERROR", "mensaje": "Usuario/clave erroneo"}, 200
    except Exception as e:
        print(f"Excepción al validar al usuario: {str(e)}", file=sys.stdout)
        return {"status": "ERROR"}, 500


