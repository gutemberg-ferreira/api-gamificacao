from flask import jsonify, request
from flasgger import swag_from
from app import app

@app.route('/', methods=['GET'])
@swag_from('../../api_docs/Rule_Events/Get_All_Rule_Events.yml')
def get_all_events():
    output = {"msg": "I'm the router_test endpoint from blueprint_x."}
    return jsonify(output)