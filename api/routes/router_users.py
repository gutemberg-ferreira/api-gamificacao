from flask import jsonify, request
from flasgger import swag_from
from api.models.users import Users, users_schema, user_schema, user_by_username
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash
from app import app, db


# note: global variables can be accessed from view functions

# add view function to the blueprint
@app.route('/all', methods=['GET'])
@jwt_required()
@swag_from('../../api_docs/Users/Get_All_Users.yml')
def get_users():
    name = request.args.get('name')
    if name:
        users = Users.query.filter(Users.name.like(f'%{name}%')).all()
    else:
        users = Users.query.all()
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
    user = Users(username, pass_hash, name, email)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'successfully registered', 'data': result.data}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500

