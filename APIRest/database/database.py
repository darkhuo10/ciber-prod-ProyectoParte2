import os
import pymysql

def obtener_conexion():
    return pymysql.connect(host="localhost",
                                user="root",
                                password="admin",
                                port=3306,
                                db="restaurant")