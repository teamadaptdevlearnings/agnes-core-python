from flask import Blueprint, Response, request, jsonify
from config.database import db
from .models import Users

users_bp = Blueprint('users', __name__)


@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = Users(
        name=data.get('name'),
        email=data.get('email'),
        password=data.get('password')
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'New user created!'}), 201


@users_bp.route('/users', methods=['GET'])
def get_users():
    users = Users.query.all()
    user_list = []
    for user in users:
        user_data = dict()
        user_data['id'] = user.id
        user_data['name'] = user.name
        user_data['email'] = user.email
        user_data['date_created'] = user.date_created
        user_list.append(user_data)
    return jsonify({'users': user_list}), 200


@users_bp.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = Users.query.filter_by(id=id).first()
    if not user:
        return jsonify({'message': 'No user found!'}), 404

    user_data = dict()
    user_data['id'] = user.id
    user_data['name'] = user.name
    user_data['email'] = user.email
    user_data['date_created'] = user.date_created
    return jsonify({'user': user_data}), 200


@users_bp.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = Users.query.filter_by(id=id).first()

    if not user:
        return jsonify({'message': 'No user found!'}), 404

    user.name = data.get('name')
    user.email = data.get('email')
    user.password = data.get('password')
    db.session.commit()
    return jsonify({'message': 'The user has been updated!'}), 200


@users_bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = Users.query.filter_by(id=id).first()
    if not user:
        return jsonify({'message': 'No user found!'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'The user has been deleted!'}), 200
