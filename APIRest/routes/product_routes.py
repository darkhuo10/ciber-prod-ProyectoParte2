from flask import request, session
import json
import decimal
from __main__ import app
from controllers import product_controller

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

@app.route("/products",methods=["GET"])
def get_all_products():
    products,code= product_controller.get_all_products()
    return json.dumps(products, cls = Encoder),code

@app.route("/product/<id>",methods=["GET"])
def get_product_by_id(id):
    product,code = product_controller.get_product_by_id(id)
    return json.dumps(product, cls = Encoder),code

@app.route("/product/create",methods=["POST"])
def create_product():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        product_json = request.json
        ret,code=product_controller.create_product(product_json) #Check if need to pass to object again
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/product/delete/<id>", methods=["DELETE"])
def delete_product(id):
    ret,code=product_controller.delete_product(id)
    return json.dumps(ret), code

@app.route("/product", methods=["PUT"])
def update_product():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        product_json = request.json
        ret,code=product_controller.update_product(product_json)
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code