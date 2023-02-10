from app import db, ma
from flask_login import UserMixin

class USERS(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, id, username, password, name, email):
        self.id = id
        self.username = username
        self.password = password
        self.name = name
        self.email = email


class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'name', 'email', 'password')


def user_by_username(username):
    try:
        return USERS.query.filter(USERS.username == username).one()
    except:
        return None

def get_user(user_id):
    user = USERS.query.filter_by(id=user_id).first()
    return user

user_schema = UsersSchema()
users_schema = UsersSchema(strict=True, many=True)
