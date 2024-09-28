from flask import Blueprint, request, jsonify
from models import create_train
from functools import wraps
from config import ADMIN_API_KEY

admin_bp = Blueprint('admin', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers.get('X-API-KEY') != ADMIN_API_KEY:
            return jsonify({'error': 'Unauthorized'}), 403
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/admin/add_train', methods=['POST'])
@admin_required
def add_train():
    data = request.get_json()
    train_name = data['train_name']
    source = data['source']
    destination = data['destination']
    total_seats = data['total_seats']
    # Insert into the database
    create_train(train_name, source, destination, total_seats)
    return jsonify({'message': 'Train added successfully'})
