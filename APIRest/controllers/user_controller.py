from __future__ import print_function
from database import database
from models.models import User
import sys


def create_user(user: User):
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO users(id_waiter, username, is_admin, password) VALUES (%s, %s, %s, %s)",
                           (user.id_waiter, user.username, user.is_admin, user.password))
            if cursor.rowcount == 1:
                ret = {"status": "OK"}
            else:
                ret = {"status": "Failure"}
        code = 200
        conexion.commit()
        conexion.close()
    except:
        print("Error al crear el usuario", file=sys.stdout)
        ret = {"status": "Failure"}
        code = 500
    return ret, code

#check si deberíamos ponerlo
def get_all_users():
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            users_json = []
            if users:
                for u in users:
                    users_json.append(u.to_json())
        conexion.close()
        code = 200
    except:
        print("Error al obtener los usuarios", file=sys.stdout)
        users_json = []
        code = 500
    return users_json, code


def get_user_by_id(id: int):
    user_json = {}
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id = %s", (id))
            user = cursor.fetchone()
            if user is not None:
                user_json = user.to_json()
        conexion.close()
        code = 200
    except:
        print("Error al recuperar el producto", file=sys.stdout)
        code = 500
    return user_json, code

# posiblemente borrar a mi no otros usuarios
def delete_user(id: int):
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE id = %s", (id))
            if cursor.rowcount == 1:
                ret = {"status": "OK"}
            else:
                ret = {"status": "Failure"}
        conexion.commit()
        conexion.close()
        code = 200
    except:
        print("Error al eliminar el usuario", file=sys.stdout)
        ret = {"status": "Failure"}
        code = 500
    return ret, code


def update_user(user: User):
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute(
                "UPDATE users SET id_waiter = %s, username = %s, is_admin = %s, password=%s WHERE id = %s",
                (user.id_waiter, user.username, user.is_admin, user.password, user.id))
            if cursor.rowcount == 1:
                ret = {"status": "OK"}
            else:
                ret = {"status": "Failure"}
        conexion.commit()
        conexion.close()
        code = 200
    except:
        print("Error al actualizar el usuario", file=sys.stdout)
        ret = {"status": "Failure"}
        code = 500
    return ret, code
