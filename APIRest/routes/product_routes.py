from flask import request, session, jsonify
import json
import decimal
from __main__ import app
from controllers import product_controller
from models.models import Product

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)

def json_to_product(product_json):
    product = Product(
        product_json.get('name'),
        product_json.get('number'),
        product_json.get('description'),
        product_json.get('price'),
        product_json.get('tax'))
    return product

@app.route("/products",methods=["GET"])
def get_all_products():
    products,code= product_controller.get_all_products()
    return jsonify(products), code
@app.route("/product/<id>",methods=["GET"])
def get_product_by_id(id):
    product,code = product_controller.get_product_by_id(id)
    return jsonify(product), code
@app.route("/product/create",methods=["POST"])
def create_product():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        product_json = request.json
        ret,code=product_controller.create_product(json_to_product(product_json)) 
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/product/delete/<id>", methods=["DELETE"])
def delete_product(id):
    ret,code=product_controller.delete_product(id)
    return json.dumps(ret), code

@app.route("/product/update/<id>", methods=["PUT"])
def update_product(id):
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        product_json = request.json
        ret,code=product_controller.update_product(json_to_product(product_json), id)
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code