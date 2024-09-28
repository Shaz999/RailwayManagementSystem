from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from models import get_user_by_username, check_availability, book_seat

user_bp = Blueprint('user', __name__)

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = get_user_by_username(username)
    if user and check_password(user['password_hash'], password):
        token = create_access_token(identity=user['id'])
        return jsonify({'token': token})
    return jsonify({'error': 'Invalid credentials'}), 401

@user_bp.route('/book', methods=['POST'])
@jwt_required
def book():
    data = request.get_json()
    user_id = get_jwt_identity()
    train_id = data['train_id']
    result = book_seat(user_id, train_id)
    return result
