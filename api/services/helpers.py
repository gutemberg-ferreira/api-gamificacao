import datetime
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from api.models.users import user_by_username
from werkzeug.security import check_password_hash


def auth():
    auth = request.headers
    if not auth or not auth.environ['HTTP_USERNAME'] or not auth.environ['HTTP_PASSWORD']:
        return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    user = user_by_username(auth.environ['HTTP_USERNAME'])
    if not user:
        return jsonify({'message': 'user not found', 'data': []}), 401


    if user and check_password_hash(user.password, auth.environ['HTTP_PASSWORD']):
        token = create_access_token(identity=auth.environ['HTTP_USERNAME'])
        return jsonify({'message': 'Validated successfully', 'token': 'Bearer '+token, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401


