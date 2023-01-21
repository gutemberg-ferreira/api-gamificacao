

"""Retorna usuário específico pelo ID no parametro da request"""


def get_user(id):
    user = Users.query.get(id)
    if user:
        result = user_schema.dump(user)
        return jsonify({'message': 'successfully fetched', 'data': result.data}), 201

    return jsonify({'message': "user don't exist", 'data': {}}), 404


"""Cadastro de usuários com validação de existência"""


"""Atualiza usuário baseado no ID, caso o mesmo exista."""


def update_user(id):
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']
    user = Users.query.get(id)

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


"""Deleta usuário com base no ID da request"""


def delete_user(id):
    user = Users.query.get(id)
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


