from database.database import obtener_conexion
import json

def create_product(data):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            query = "INSERT INTO product (name, description, number, price) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (data['name'], data.get('description'), data['number'], data['price']))
            conn.commit()
            cursor.close()
            conn.close()
            ret = {"status": "OK", "message": "Product created successfully"}
            code = 200
        except Exception as e:
            print(f"Exception while creating product: {e}")
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code

def get_product(product_id):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            query = "SELECT * FROM product WHERE id = %s"
            cursor.execute(query, (product_id,))
            product = cursor.fetchone()
            cursor.close()
            conn.close()
            if product is None:
                ret = {"status": "ERROR", "message": "Product not found"}
                code = 404
            else:
                ret = {"status": "OK", "product": product}
                code = 200
        except Exception as e:
            print(f"Exception while fetching product: {e}")
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code

def update_product(product_id, data):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            query = "UPDATE product SET name = %s, description = %s, number = %s, price = %s WHERE id = %s"
            cursor.execute(query, (data['name'], data.get('description'), data['number'], data['price'], product_id))
            conn.commit()
            cursor.close()
            conn.close()
            ret = {"status": "OK", "message": "Product updated successfully"}
            code = 200
        except Exception as e:
            print(f"Exception while updating product: {e}")
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code

def delete_product(product_id):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            query = "DELETE FROM product WHERE id = %s"
            cursor.execute(query, (product_id,))
            conn.commit()
            cursor.close()
            conn.close()
            ret = {"status": "OK", "message": "Product deleted successfully"}
            code = 200
        except Exception as e:
            print(f"Exception while deleting product: {e}")
            ret = {"status": "ERROR"}
            code = 500
    else:
        ret = {"status": "Bad request"}
        code = 401
    return json.dumps(ret), code
