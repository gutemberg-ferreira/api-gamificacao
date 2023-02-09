import os

from flask import Flask
from flasgger import Swagger
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

template = 'api_docs/swagger.yml'

template_dir = os.path.abspath('./web/templates/')
static_dir = os.path.abspath('./web/static/')
app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)
app.config.from_object('config')
CORS(app)
swagger = Swagger(app, template_file=template)
ma = Marshmallow(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)
db.create_all()

from api.routes.router_listen_events import *
from api.routes.router_rule_events import *
from api.routes.router_rank import *
from api.routes.router_auth import *
from api.routes.router_users import *
from api.routes.router_campaigns_bonus import *
from api.routes.router_dash_rank import *