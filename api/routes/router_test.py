from flask import jsonify, request
from flasgger import swag_from
from flask_cors import cross_origin

from app import app
# note: global variables can be accessed from view functions
x = 5


# add view function to the blueprint
@app.route("/")
@cross_origin()
@swag_from('../../api_docs/Tests/Router_Test_Get_Root.yml')
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/test', methods=['GET'])
@cross_origin()
@swag_from('../../api_docs/Tests/Router_Test_Get_Test.yml')
def test():
    output = {"msg": "I'm the router_test endpoint from blueprint_x."}
    return jsonify(output)


# add view function to the blueprint
@app.route('/plus', methods=['POST'])
@cross_origin()
@swag_from('../../api_docs/Tests/Router_Test_Post_Sun.yml')
def plus_x():
    # retrieve body data from input JSON
    data = request.get_json()
    in_val = data['number']
    # compute result and output as JSON
    result = in_val + x
    output = {"msg": f"Your result is: '{result}'"}
    return jsonify(output)