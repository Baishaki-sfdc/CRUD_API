# routes/user_routes.py
import re
from flask import Blueprint, jsonify, request, abort
from models.user import User
from database.db import db

user_bp = Blueprint('user_bp', __name__)

# Validation of user data
def validate_user_data(data, required_fields=True):
    """
    Validate incoming user data.
    If required_fields is True, all fields must be present.
    If False, only validate the fields that are provided.
    """
    errors = []
    # Check for required fields if needed
    if required_fields:
        for field in ["name", "email", "age"]:
            if field not in data:
                errors.append(f"Missing required field: {field}")
    # Validate name
    if "name" in data and not isinstance(data["name"], str):
        errors.append("Field 'name' must be a string.")
    # Validate email and its format
    if "email" in data:
        if not isinstance(data["email"], str):
            errors.append("Field 'email' must be a string.")
        else:
            # Basic email regex (simple validation)
            pattern = r'^\S+@\S+\.\S+$'
            if not re.match(pattern, data["email"]):
                errors.append("Field 'email' must be a valid email address.")
    # Validate age
    if "age" in data:
        try:
            age_val = int(data["age"])
            if age_val < 0:
                errors.append("Field 'age' must be a positive integer.")
        except (ValueError, TypeError):
            errors.append("Field 'age' must be an integer.")
    return errors

# Create a User
@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        abort(400, description="No input data provided.")
    
    # Validate input data
    errors = validate_user_data(data, required_fields=True)
    if errors:
        abort(400, description="; ".join(errors))
    
    # Existing functionality to create a user
    user = User(name=data["name"], email=data["email"], age=int(data["age"]))
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(400, description="Error saving user: " + str(e))
    return jsonify(user.to_dict()), 201

# Retrieve All Users
@user_bp.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

# Retrieve a Single User
@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404, description="User not found.")
    return jsonify(user.to_dict()), 200

# Update a User
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if not data:
        abort(400, description="No update data provided.")
    
    # Validate provided update data (fields are optional)
    errors = validate_user_data(data, required_fields=False)
    if errors:
        abort(400, description="; ".join(errors))
    
    user = User.query.get(user_id)
    if not user:
        abort(404, description="User not found.")
    
    # Update user details if provided
    if "name" in data:
        user.name = data["name"]
    if "email" in data:
        user.email = data["email"]
    if "age" in data:
        user.age = int(data["age"])
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(400, description="Error updating user: " + str(e))
    return jsonify(user.to_dict()), 200

# Delete a User
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404, description="User not found.")
    try:
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(400, description="Error deleting user: " + str(e))
    return jsonify({"message": "User deleted successfully."}), 200
