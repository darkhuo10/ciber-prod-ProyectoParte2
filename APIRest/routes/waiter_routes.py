from flask import Blueprint, request, jsonify
from controllers.waiter_controller import create_waiter, get_waiter, update_waiter, delete_waiter

waiter_bp = Blueprint('waiter_bp', __name__)

@waiter_bp.route('/waiter/create', methods=['POST'])
def create_waiter_route():
    return jsonify(create_waiter(request.json)), 201

@waiter_bp.route('/waiters/<int:waiter_id>', methods=['GET'])
def get_waiter_route(waiter_id):
    waiter = get_waiter(waiter_id)
    if waiter:
        return jsonify(waiter)
    return jsonify({"error": "Waiter not found"}), 404

@waiter_bp.route('/waiters/<int:waiter_id>', methods=['PUT'])
def update_waiter_route(waiter_id):
    return jsonify(update_waiter(waiter_id, request.json))

@waiter_bp.route('/waiters/<int:waiter_id>', methods=['DELETE'])
def delete_waiter_route(waiter_id):
    return jsonify(delete_waiter(waiter_id))

@waiter_bp.route('/test', methods=['GET'])
def test():
    return jsonify("Hello")
