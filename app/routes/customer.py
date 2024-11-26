import random
import string
from flask import Blueprint, request, jsonify, session
from app import db
from app.models import Customer
import africastalking
import os
from functools import wraps

# Initialize the blueprint
customer_bp = Blueprint('customers', __name__)

# Load SMS configuration from environment variables
SMS_USERNAME = os.getenv('AFRICASTALKING_USERNAME')
SMS_API_KEY = os.getenv('AFRICASTALKING_API_KEY')

# Initialize Africa's Talking SMS
africastalking.initialize(SMS_USERNAME, SMS_API_KEY)
sms = africastalking.SMS


def generate_unique_code(length=6):
    """
    Generate a unique alphanumeric code for the customer.
    Ensure the code does not already exist in the database.
    """
    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        if not Customer.query.filter_by(code=code).first():  # Ensure the code is unique
            return code


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


@customer_bp.route('/', methods=['POST'])
@login_required
def create_customer():
    data = request.get_json()
    
    # Validate the input
    if not data or 'name' not in data or 'phone' not in data:
        return jsonify({'error': 'Missing required fields: name and phone'}), 400

    # Generate a unique code for the customer
    code = generate_unique_code()

    # Create the customer
    customer = Customer(name=data['name'], code=code)
    db.session.add(customer)
    db.session.commit()

    # Send SMS to the customer
    try:
        phone_number = data['phone']
        message = f"Hello {customer.name}, your customer account with code {customer.code} has been created successfully!"
        response = sms.send(message, [phone_number])

        return jsonify({
            'message': 'Customer created successfully and SMS sent!',
            'id': customer.id,
            'code': customer.code,
            'sms_response': response
        }), 201

    except Exception as e:
        return jsonify({'error': f"Customer created, but failed to send SMS: {str(e)}"}), 500


@customer_bp.route('/', methods=['GET'])
@login_required
def get_customers():
    customers = Customer.query.all()
    return jsonify([{'id': c.id, 'name': c.name, 'code': c.code} for c in customers])
