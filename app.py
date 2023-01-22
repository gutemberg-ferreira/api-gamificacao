from flask import Flask, jsonify
from flasgger import Swagger
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


template = {
      "swagger": "2.0",
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
      },
      "host": "localhost:5000",  # overrides localhost:500
      "basePath": "/",
      "operationId": "getmyData"
}


app = Flask(__name__)
app.config.from_object('config')
swagger = Swagger(app, template=template)
ma = Marshmallow(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)
db.create_all()

from api.routes.router_users import Users
from api.routes.router_test import test
from api.routes.router_rule_events import RuleEvents
from api.routes.router_auth import authenticate