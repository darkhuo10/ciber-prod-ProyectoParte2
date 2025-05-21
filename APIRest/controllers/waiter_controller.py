from __future__ import print_function
from database import database
from models.models import Waiter
import sys
import traceback
from flask_wtf.csrf import generate_csrf
import datetime as dt
from APIRest.common.functions import compare_password, cipher_password,create_session
from __main__ import app

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
        "password": row[9],
        "lastaccess": row[10],
        "loginerror": row[11]
    }



def create_waiter(waiter: Waiter):
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute(
                "INSERT INTO waiters(identification, firstname, lastname1, lastname2, phone, email, username, password) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (waiter.identification, waiter.firstname, waiter.lastname1, waiter.lastname2, waiter.phone,
                 waiter.email, waiter.username, cipher_password(waiter.password))
            )
            
            # Check if the row was inserted successfully
            if cursor.rowcount == 1:
                ret = {"status": "OK"}
            else:
                ret = {"status": "Failure"}
        
        # Commit the transaction
        conexion.commit()
        conexion.close()

    except Exception as e:
        # Capture the exception and log the error message for debugging
        print("Error al crear el camarero:", file=sys.stdout)
        print(str(e), file=sys.stdout)
        print(traceback.format_exc(), file=sys.stdout)  # This prints the full traceback for better debugging
        ret = {"status": "Failure"}
        code = 500
    else:
        code = 200  # Success code
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


def update_waiter(waiter: Waiter, id: int):
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute(
                "UPDATE waiters SET identification = %s, firstname = %s, lastname1 = %s, lastname2=%s, phone=%s, email=%s, username=%s, password=%s WHERE id = %s",
                (waiter.identification, waiter.firstname, waiter.lastname1, waiter.lastname2, waiter.phone, waiter.email, waiter.username, waiter.password, id))
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

def login_user(username, passwordIn):
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT isadmin, password, loginerror FROM waiters WHERE username = %s", (username,))
            user = cursor.fetchone()

            if user is None:
                ret = {"status": "ERROR", "mensaje": "Usuario/clave erroneo"}
            else:
                isadmin = user[0]
                stored_password = user[1]
                numAccesosErroneos = user[2]

                if compare_password(stored_password.encode("utf-8"), passwordIn.encode("utf-8")):
                    ret = {
                        "status": "OK",
                        "csrf_token": generate_csrf(),
                        "isadmin": isadmin
                    }
                    app.logger.info("Acceso usuario %s correcto", username)
                    create_session(username, isadmin)
                    numAccesosErroneos = 0
                else:
                    app.logger.info("Acceso usuario %s incorrecto", username)
                    numAccesosErroneos += 1
                    ret = {"status": "ERROR", "mensaje": "Usuario/clave erroneo"}

                today = dt.date.today().strftime('%Y-%m-%d')
                cursor.execute("UPDATE waiters SET loginerror = %s, lastaccess = %s WHERE username = %s",
                               (numAccesosErroneos, today, username))
                conexion.commit()

        conexion.close()
        code = 200

    except Exception as e:
        print("Excepcion al validar al usuario:", e, file=sys.stdout)
        print(traceback.format_exc(), file=sys.stdout)
        ret = {"status": "ERROR"}
        code = 500

    return ret, code
