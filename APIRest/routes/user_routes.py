from flask import Flask, request, session, json

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Necesario para usar sesiones

def obtener_conexion():
    # Implementar la lógica de conexión a la base de datos aquí
    pass

@app.route("/login", methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        usuario_json = request.json
        username = usuario_json['username']
        password = usuario_json['password']
        try:
            conexion = obtener_conexion()
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id, idwaiter, username FROM Users WHERE username = %s and password = %s", (username, password))
                usuario = cursor.fetchone()
            conexion.close()
            if usuario is None:
                ret = {"status": "ERROR", "mensaje": "Usuario/clave erroneo"}
            else:
                session["usuario"] = {
                    "id": usuario[0],
                    "idwaiter": usuario[1],
                    "username": usuario[2]
                }
                ret = {"status": "OK"}
            code = 200
        except:
            print("Excepcion al validar al usuario")
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code

@app.route("/register", methods=['POST'])
def registro():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        usuario_json = request.json
        idwaiter = usuario_json['idwaiter']
        username = usuario_json['username']
        password = usuario_json['password']
        try:
            conexion = obtener_conexion()
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id FROM Users WHERE username = %s", (username,))
                usuario = cursor.fetchone()
                if usuario is None:
                    cursor.execute("INSERT INTO Users (idwaiter, username, password) VALUES (%s, %s, %s)", (idwaiter, username, password))
                    if cursor.rowcount == 1:
                        conexion.commit()
                        ret = {"status": "OK"}
                        code = 200
                    else:
                        ret = {"status": "ERROR"}
                        code = 500
                else:
                    ret = {"status": "ERROR", "mensaje": "Usuario ya existe"}
                    code = 200
            conexion.close()
        except:
            print("Excepcion al registrar al usuario")
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code

@app.route("/me", methods=['GET'])
def me():
    if "usuario" in session:
        ret = {
            "status": "OK",
            "usuario": session["usuario"]
        }
        code = 200
    else:
        ret = {"status": "ERROR", "mensaje": "No hay usuario logueado"}
        code = 401
    return json.dumps(ret), code

@app.route("/logout", methods=['GET'])
def logout():
    session.clear()
    return json.dumps({"status": "OK"}), 200

if __name__ == "__main__":
    app.run()
