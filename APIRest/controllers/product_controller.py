from __future__ import print_function
from database import database
from models.models import Product
import sys
import traceback

def product_to_json(row):
    #name: str, number: int, description: str, price: float, tax: float, image: str
    return {
        "id": row[0],
        "name": row[1],
        "number": row[2],
        "description": row[3],
        "price": str(row[4]),
        "tax": row[5]
    }

def create_product(product: Product):
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute(
                "INSERT INTO products(name, description, number, price, tax) VALUES (%s, %s, %s, %s, %s)",
                (product.name, product.description, product.number, product.price, product.tax)
            )

            # Check if the row was inserted successfully
            if cursor.rowcount == 1:
                ret = {"status": "OK"}
            else:
                ret = {"status": "Failure"}

        # Commit and close
        conexion.commit()
        conexion.close()

    except Exception as e:
        # Error handling and detailed traceback
        print("Error al crear el producto:", file=sys.stdout)
        print(str(e), file=sys.stdout)
        print(traceback.format_exc(), file=sys.stdout)
        ret = {"status": "Failure"}
        code = 500
    else:
        code = 200  # Success code
    return ret, code

def get_all_products():
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
            products_json=[]
            if products:
                for p in products:
                    products_json.append(product_to_json(p))
        conexion.close()
        code=200
    except:
        print("Error al obtener los productos", file=sys.stdout)
        products_json=[]
        code=500
    return products_json, code

def get_product_by_id(id: int):
    product_json = {}
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM products WHERE id = %s", (id))
            product = cursor.fetchone()
            if product is not None:
                product_json = product_to_json(product)
        conexion.close()
        code=200
    except:
        print("Error al recuperar el producto", file=sys.stdout)
        code=500
    return product_json, code


def delete_product(id: int):
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM products WHERE id = %s", (id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Error al eliminar el producto", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code

def update_product(product: Product, id: int):
    try:
        conexion = database.get_dbc()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE products SET name = %s, description = %s, number = %s, price=%s, tax= %s WHERE id = %s",
                       (product.name, product.description, product.number, product.price, product.tax, id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        print("Error al actualizar el producto", file=sys.stdout)
        ret = {"status": "Failure" }
        code=500
    return ret,code
