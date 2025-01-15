

from flask import Blueprint, jsonify , request
from .models import db, Task
from flask_jwt_extended import create_access_token
from .models import User
from flask_jwt_extended import jwt_required, get_jwt_identity

api_bp = Blueprint('api', __name__)




@api_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Check if the user exists
    user = User.query.filter_by(email=email).first()
    if not user or user.password != password:
        return jsonify({"error": "Invalid credentials"}), 401

    # Convert user ID to string when creating the token
    access_token = create_access_token(identity=str(user.id))
    return jsonify({"access_token": access_token})

@api_bp.route('/')
def home():
    return jsonify({"message": "Welcome to the Task Management API!"})



# Get all tasks (protected)
@api_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    current_user_id = get_jwt_identity()  # Get user ID from the token
    tasks = Task.query.filter_by(user_id=current_user_id).all()
    return jsonify([
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "created_at": task.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "is_completed": task.is_completed,
        } for task in tasks
    ])

# Create a new task (protected)
@api_bp.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    current_user_id = get_jwt_identity()  # Get the logged-in user's ID
    data = request.get_json()

    new_task = Task(
        title=data['title'],
        description=data.get('description', ''),
        is_completed=data.get('is_completed', False),
        user_id=current_user_id  # Assign the logged-in user as the task owner
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created successfully!", "task_id": new_task.id}), 201

@api_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()

    # Update the task fields
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.is_completed = data.get('is_completed', task.is_completed)
    task.user_id = data.get('user_id', task.user_id)  # Optional update

    db.session.commit()
    return jsonify({"message": "Task updated successfully!"})

@api_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully!"})

@api_bp.route('/debug/tasks', methods=['GET'])
def debug_tasks():
    tasks = Task.query.all()
    return jsonify([
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "created_at": task.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "is_completed": task.is_completed,
            "user_id": task.user_id
        } for task in tasks
    ])
