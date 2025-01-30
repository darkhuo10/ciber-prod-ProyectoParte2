from flask import Blueprint, request, jsonify
from controllers.user_controller import create_user, get_user, update_user, delete_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user_route():
    return jsonify(create_user(request.json))

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_route(user_id):
    return jsonify(get_user(user_id))

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    return jsonify(update_user(user_id, request.json))

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    return jsonify(delete_user(user_id))