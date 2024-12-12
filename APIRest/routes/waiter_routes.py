from flask import Blueprint
from controllers.waiter_controller import create_waiter, get_all_waiters, get_waiter, update_waiter, delete_waiter

waiter_bp = Blueprint('waiters', __name__)

# Route to create a new waiter
waiter_bp.route('/create', methods=['POST'])(create_waiter)

# Route to get all waiters
waiter_bp.route('/waiters', methods=['GET'])(get_all_waiters)

# Route to get a specific waiter by ID
waiter_bp.route('/waiters/<int:id>', methods=['GET'])(get_waiter)

# Route to update a specific waiter by ID
waiter_bp.route('/waiters/<int:id>', methods=['PUT'])(update_waiter)

# Route to delete a specific waiter by ID
waiter_bp.route('/waiters/<int:id>', methods=['DELETE'])(delete_waiter)
