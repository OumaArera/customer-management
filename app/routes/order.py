from flask import Blueprint, request, jsonify, session
from app import db
from app.models import Order, Customer
from app.services.sms_service import send_sms
from functools import wraps

# Initialize the blueprint
order_bp = Blueprint('orders', __name__)

def login_required(f):
    """
    Decorator to enforce that the user is logged in.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return jsonify({'error': 'Unauthorized access. Please log in.'}), 401
        return f(*args, **kwargs)
    return decorated_function

@order_bp.route('/', methods=['POST'])
@login_required
def create_order():
    data = request.get_json()

    # Validate input
    if not data or 'customer_id' not in data or 'item' not in data or 'amount' not in data:
        return jsonify({'error': 'Missing required fields: customer_id, item, or amount'}), 400

    # Check if customer exists
    customer = Customer.query.get(data['customer_id'])
    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    # Create the order
    order = Order(
        customer_id=data['customer_id'],
        item=data['item'],
        amount=data['amount']
    )
    db.session.add(order)
    db.session.commit()

    # Send SMS notification
    try:
        message = f"Dear {customer.name}, your order for {order.item} has been placed successfully."
        send_sms(customer.code, message)
        return jsonify({'message': 'Order created successfully', 'id': order.id}), 201
    except Exception as e:
        return jsonify({'error': f"Order created, but SMS failed: {str(e)}"}), 500
