from flask import jsonify, request
from flasgger import swag_from
from api.models.users import USERS, users_schema, user_schema, user_by_username
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash
from app import app, db


@app.route('/all', methods=['GET'])
@jwt_required()
@swag_from('../../api_docs/Users/Get_All_Users.yml')
def get_users():
    name = request.args.get('name')
    if name:
        users = USERS.query.filter(USERS.name.like(f'%{name}%')).all()
    else:
        users = USERS.query.all()
    if users:
        result = users_schema.dump(users)
        return jsonify({'message': 'successfully fetched', 'data': result.data})

    return jsonify({'message': 'nothing found', 'data': {}})


@app.route('/addUser', methods=['POST'])
@jwt_required()
@swag_from('../../api_docs/Users/Post_New_User.yml')
def post_user():
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    user = user_by_username(username)
    if user:
        result = user_schema.dump(user)
        return jsonify({'message': 'user already exists', 'data': {}})

    pass_hash = generate_password_hash(password)
    user = USERS(username, pass_hash, name, email)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'successfully registered', 'data': result.data}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500


@app.route('/updateUserID/<int:id>', methods=['PATCH'])
@jwt_required()
@swag_from('../../api_docs/Users/Path_User_Id.yml')
def update_user(id):
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']
    user = USERS.query.get(id)

    if not user:
        return jsonify({'message': "user don't exist", 'data': {}}), 404

    pass_hash = generate_password_hash(password)

    if user:
        try:
            user.username = username
            user.password = pass_hash
            user.name = name
            user.email = email
            db.session.commit()
            result = user_schema.dump(user)
            return jsonify({'message': 'successfully updated', 'data': result.data}), 201
        except:
            return jsonify({'message': 'unable to update', 'data':{}}), 500


@app.route('/deleteUserID/<int:id>', methods=['DELETE'])
@jwt_required()
@swag_from('../../api_docs/Users/Delete_User_Id.yml')
def delete_user(id):
    user = USERS.query.get(id)
    if not user:
        return jsonify({'message': "user don't exist", 'data': {}}), 404

    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            result = user_schema.dump(user)
            return jsonify({'message': 'successfully deleted', 'data': result.data}), 200
        except:
            return jsonify({'message': 'unable to delete', 'data': {}}), 500


@app.route('/getUserID/<int:id>', methods=['GET'])
@jwt_required()
@swag_from('../../api_docs/Users/Get_User_Id.yml')
def get_user(id):
    user = USERS.query.get(id)
    if user:
        result = user_schema.dump(user)
        return jsonify({'message': 'successfully fetched', 'data': result.data}), 201

    return jsonify({'message': "user don't exist", 'data': {}}), 404