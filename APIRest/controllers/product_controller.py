from __future__ import print_function
from common.functions import sanitize_input
from database.database import get_dbc
from __main__ import app

def product_to_json(product):
    return {
        'id': product[0],
        'name': sanitize_input(product[1]),
        'description': sanitize_input(product[2]),
        'number': product[3],
        'price': product[4],
        'tax': product[5]
    }



def create_product(name, description, number, price, tax):
    ret = {"status": "Failure"}
    code = 500
    try:
        conn = get_dbc()
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO products(name, description, number, price, tax) VALUES (%s, %s, %s, %s, %s)",
                (name, description, number, price, tax)
            )
            if cursor.rowcount == 1:
                ret = {"status": "OK"}
                code = 200
            else:
                code = 400  # or some failure code

        conn.commit()
        conn.close()

    except Exception as e:
        app.logger.error(f"Excepcion al insertar un producto: {e}")
        ret = {"status": "Failure"}
        code = 500
    return ret, code



def get_all_products():
    products_json = []
    code = 500
    conn = None
    try:
        conn = get_dbc()
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, name, description, number, price, tax FROM products")
            products = cursor.fetchall()
            if products:
                for p in products:
                    products_json.append(product_to_json(p))
        code = 200
    except Exception as e:
        app.logger.error(f"Excepción al obtener los productos: {str(e)}")
    finally:
        if conn:
            conn.close()
    return products_json, code



def get_product_by_id(id):
    product_json = {}
    try:
        conn = get_dbc()
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, name, description, number, price, tax FROM products WHERE id = %s LIMIT 1", (id,))
            product = cursor.fetchone()
            if product is not None:
                product_json = product_to_json(product)
        conn.close()
        code=200
    except:
        app.logger.info("Excepcion al consultar un producto")
        code=500
    return product_json, code


def delete_product(id):
    try:
        conn = get_dbc()
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM products WHERE id = %s", (id,))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conn.commit()
        conn.close()
        code=200
    except:
        app.logger.info("Excepcion al eliminar un producto")
        ret = {"status": "Failure" }
        code=500
    return ret,code


def update_product(id, name, description, number, price, tax):
    try:
        conn = get_dbc()
        with conn.cursor() as cursor:
            cursor.execute("UPDATE products SET name = %s, description = %s, number = %s, price=%s, tax= %s WHERE id = %s",
                       (name, description, number, price, tax, id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conn.commit()
        conn.close()
        code=200
    except:
        app.logger.info("Excepcion al actualziar un producto")
        ret = {"status": "Failure" }
        code=500
    return ret,code