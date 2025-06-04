from flask_wtf.csrf import generate_csrf
from database.database import get_dbc
from common.functions import compare_password, cipher_password, create_session
import sys
import datetime as dt
from __main__ import app

import datetime as dt

def login_usuario(username, passwordIn):
    try:
        conexion = get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT role, passwd, login_errors FROM users WHERE activity='active' and username = %s",
                (username,)  # <-- coma para tupla
            )
            user = cursor.fetchone()
            
            if user is None:
                ret = {"status": "ERROR", "mensaje": "Usuario/clave erroneo"}
            else:
                role, password, login_errors = user

                current_date = dt.date.today()
                hoy = current_date.strftime('%Y-%m-%d')
                    
                if compare_password(password.encode("utf-8"), passwordIn.encode("utf-8")):
                    ret = {
                        "status": "OK",
                        "csrf_token": generate_csrf(),
                        "role": role
                    }
                    app.logger.info("Acceso user %s correcto", username)
                    create_session(username, role)
                    login_errors = 0
                    activity = 'active'
                else:
                    app.logger.info("Acceso user %s incorrecto", username)
                    login_errors += 1
                    if login_errors > 2:
                        activity = "inactive"
                        app.logger.info("Usuario %s inactive", username)
                    else:
                        activity = 'active'
                    ret = {"status": "ERROR", "mensaje": "Usuario/clave erroneo"}
                
                cursor.execute(
                    "UPDATE users SET login_errors=%s, last_login=%s, activity=%s WHERE username = %s",
                    (login_errors, hoy, activity, username)
                )
                conexion.commit()
            conexion.close()
            code = 200
    except Exception as e:
        print(f"Excepción al validar al user: {e}")   
        ret = {"status": "ERROR"}
        code = 500
    return ret, code


def register_user(username,password,role,email):
    try:
        conexion = get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT role FROM users WHERE username = %s",(username,))
            user = cursor.fetchone()
            if user is None:
                passwordC=cipher_password(password)
                cursor.execute("INSERT INTO users(username,passwd,email,role,activity,login_errors) VALUES(%s,%s,%s,'user','active',0)",(username,passwordC,email))
                if cursor.rowcount == 1:
                    conexion.commit()
                    app.logger.info("Nuevo user creado")
                    ret={"status": "OK" }
                    code=200
                else:
                    ret={"status": "ERROR" }
                    code=500
            else:
                ret = {"status": "ERROR","mensaje":"Usuario ya existe" }
                code=200
        conexion.close()
    except:
        print("Excepcion al registrar al user")   
        ret={"status":"ERROR"}
        code=500
    return ret,code    