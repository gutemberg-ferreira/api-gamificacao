from flask import Blueprint, jsonify, request
from flasgger import swag_from
router_rule_events= Blueprint(name="_ruler_events", import_name=__name__)

@router_rule_events.route('/', methods=['GET'])
@swag_from('../../api_docs/Rule_Events/Get_All_Rule_Events.yml')
def test():
    output = {"msg": "I'm the router_test endpoint from blueprint_x."}
    return jsonify(output)

# add view function to the blueprint
@router_rule_events.route('/plus', methods=['POST'])
#@swag_from('../../api_docs/Router_Test_Post_Sun.yml')
def plus_x():
    # retrieve body data from input JSON
    data = request.get_json()
    in_val = data['number']
    # compute result and output as JSON
    result = in_val + 5
    output = {"msg": f"Your result is: '{result}'"}
    return jsonify(output)