from flask import Flask, jsonify
from flasgger import Swagger
from api.routes.router_test import router_test
from api.routes.router_rule_events import router_rule_events

template = {
      "swagger": "2.0",
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
swagger = Swagger(app, template=template)

app.register_blueprint(router_test, url_prefix="/")
app.register_blueprint(router_rule_events, url_prefix="/rulesEvents")
