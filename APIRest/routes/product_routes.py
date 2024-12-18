from flask import Blueprint, request, jsonify
from controllers.product_controller import create_product, get_product, update_product, delete_product

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['POST'])
def create_product_route():
    return jsonify(create_product(request.json)), 201

@product_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product_route(product_id):
    product = get_product(product_id)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@product_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    return jsonify(update_product(product_id, request.json))

@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    return jsonify(delete_product(product_id))
