from flask import request, session, jsonify, make_response
import json
import decimal
from __main__ import app
from controllers import product_controller
from common.functions import Encoder, sanitize_input, prepare_response_extra_headers, admin_session_validate, user_session_validate

@app.route("/products",methods=["GET"])
def get_all_products():
    if user_session_validate():
        res, code= product_controller.get_all_products()
    else:
        res = {"status":"Forbidden"}
        code=403
    response= make_response(json.dumps(res, cls=Encoder), code)
    return response



@app.route("/product/<id>",methods=["GET"])
def get_product_by_id(id):
    id = sanitize_input(id)
    if isinstance(id, str) and len(id) < 64:
        res, code = product_controller.get_product_by_id(id)
    else:
        res = {"status":"Forbidden"}
        code = 403
    response = make_response(json.dumps(res, cls=Encoder), code)
    return response

@app.route("/product/create",methods=["POST"])
def create_product():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        product_json = request.json
        if "name" in product_json and "description" in product_json and "number" in product_json and "price" in product_json and "tax" in product_json:
            name = sanitize_input(str(product_json["name"]))
            description = sanitize_input(str(product_json["description"]))
            number = product_json["number"]
            price = product_json["price"]
            tax = product_json["tax"]
            if isinstance(name, str) and isinstance(description, str) and number.isnumeric() and tax.isnumeric() and len(name) < 128 and len(description) < 512:
                price = float(price)
                tax = int(tax)
                number = int(number)
                if admin_session_validate():
                    res, code = product_controller.create_product(name, description, number, price, tax)
                else:
                    res = {"status":"Forbidden"}
                    code = 403
            else:
                res = {"status": "Bad request"}
                code = 401
        else:
            res = {"status": "Bad request"}
            code = 401
    else:
        res = {"status": "Bad request"}
        code = 401
    response = make_response(json.dumps(res, cls=Encoder), code)
    return response

@app.route("/product/delete/<id>", methods=["DELETE"])
def delete_product(id):
    if admin_session_validate():
        res,code=product_controller.delete_product(id)
    else:
        res = {"status": "Forbidden"}
        code = 403
    response = make_response(json.dumps(res, cls=Encoder), code)
    return response

@app.route("/product/update", methods=["PUT"])
def update_product():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        product_json = request.json
        if "id" in product_json and "name" in product_json and "description" in product_json and "number" in product_json and "price" in product_json and "tax" in product_json:
            id = product_json["id"]
            name = sanitize_input(str(product_json["name"]))
            description = sanitize_input(str(product_json["description"]))
            number = product_json["number"]
            price = product_json["price"]
            tax = product_json["tax"]
            if id.isnumeric() and isinstance(name, str) and isinstance(description, str) and number.isnumeric() and tax.isnumeric() and len(name) < 128 and len(description) < 512:
                id = int(id)
                price = float(price)
                tax = int(tax)
                number = int(number)
                if user_session_validate():
                    res, code=product_controller.update_product(id, name, description, number, price, tax)
                else:
                    res = {"status":"Forbidden"}
                    code = 403
            else:
                res={"status":"Bad request"}
                code=401
        else:
            res={"status":"Bad request"}
            code=401       
    else:
        res={"status":"Bad request"}
        code=401
    response = make_response(json.dumps(res, cls=Encoder), code)
    return response
