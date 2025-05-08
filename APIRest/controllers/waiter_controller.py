from __future__ import print_function
from database import database
from models.models import Waiter
import sys

def waiter_to_json(row):
    return {
        "id": row[0],
        "identification": row[1],
        "firstname": row[2],
        "lastname1": row[3],
        "lastname2": row[4],
        "phone": row[5],
        "email": row[6],
        "username": row[7],
        "isadmin": row[8],
        "password": row[9]
    }

def create_waiter(waiter: Waiter):
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute(
                "INSERT INTO waiters(identification, firstname, lastname1, lastname2, phone, email, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (waiter.identification, waiter.firstname, waiter.lastname1, waiter.lastname2, waiter.phone,
                 waiter.email, waiter.username, waiter.passwordhash)
            )
            if cursor.rowcount == 1:
                ret = {"status": "OK"}
            else:
                ret = {"status": "Failure"}
        code = 200
        conexion.commit()
        conexion.close()
    except:
        print("Error al crear el camarero", file=sys.stdout)
        ret = {"status": "Failure"}
        code = 500
    return ret, code


def get_all_waiters():
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM waiters")
            waiters = cursor.fetchall()
            waiters_json = []
            if waiters:
                for w in waiters:
                    print(w.__repr__)
                    waiters_json.append(waiter_to_json(w))
        conexion.close()
        code = 200
    except:
        print("Error al obtener los camareros", file=sys.stdout)
        waiters_json = []
        code = 500
    return waiters_json, code



def get_waiter_by_id(id: int):
    waiter_json = {}
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM waiters WHERE id = %s", id)
            waiter = cursor.fetchone()
            if waiter is not None:
                waiter_json = waiter_to_json(waiter)
        conexion.close()
        code = 200
    except:
        print("Error al recuperar el camarero", file=sys.stdout)
        code = 500
    return waiter_json, code


def delete_waiter(id: int):
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM waiters WHERE id = %s", (id))
            if cursor.rowcount == 1:
                ret = {"status": "OK"}
            else:
                ret = {"status": "Failure"}
        conexion.commit()
        conexion.close()
        code = 200
    except:
        print("Error al eliminar al camarero", file=sys.stdout)
        ret = {"status": "Failure"}
        code = 500
    return ret, code


def update_waiter(waiter: Waiter):
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute(
                # (identification, firstname, lastname1, lastname2, phone, email) VALUES (%s, %s, %s, %s, %s, %s)",
                "UPDATE waiters SET identification = %s, firstname = %s, lastname1 = %s, lastname2=%s, phone=%s, email=%s WHERE id = %s",
                (waiter.identification, waiter.firstname, waiter.lastname1, waiter.lastname2, waiter.phone, waiter.email, waiter.id))
            if cursor.rowcount == 1:
                ret = {"status": "OK"}
            else:
                ret = {"status": "Failure"}
        conexion.commit()
        conexion.close()
        code = 200
    except:
        print("Error al actualizar el camareros", file=sys.stdout)
        ret = {"status": "Failure"}
        code = 500
    return ret, code
