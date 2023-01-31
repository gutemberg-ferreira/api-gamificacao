import os

from flask import Flask
from flasgger import Swagger
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

template = {
      "swagger": "2.0",
      "swaggerDefinition": {
            "info": {
                "title": "API Gamification",
                "description": "API Gamification for Nexto",
                "contact": {
                  "responsibleOrganization": "M.I.T.",
                  "responsibleDeveloper": "GB, Thiago",
                  "email": "me@me.com",
                  "url": "www.me.com",
                },
                "termsOfService": "http://me.com/terms",
                "version": "1.0.0"
              }
      },
      "securityDefinitions": {
          "APIKeyHeader": {
              "type": "apiKey",
              "name": "Authorization",
              "in": "header",
              "description": "Bearer "
          },
      },
      "security": {
        "APIKeyHeader": []
      },
      "host": "0.0.0.0:5000",
      "basePath": "/",
      "operationId": "getmyData"
}

template_dir = os.path.abspath('./web/templates/')
static_dir = os.path.abspath('./web/static/')
app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)
app.config.from_object('config')
CORS(app)
swagger = Swagger(app, template=template)
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