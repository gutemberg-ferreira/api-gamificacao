from flask import jsonify, request
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from api.models.rule_events import RuleEvents, ruleEvent_schema
from app import app, db


@app.route('/allEvents', methods=['GET'])
@jwt_required()
@swag_from('../../api_docs/Rule_Events/Get_All_Rule_Events.yml')
def get_all_rule_events():
    nameEvent = request.args.get('events')
    if nameEvent:
        event = RuleEvents.query.filter(RuleEvents.name.like(f'%{nameEvent}%')).all()
    else:
        event = RuleEvents.query.all()
    if event:
        result = ruleEvent_schema.dump(event)
        return jsonify({'message': 'successfully fetched', 'data': result.data})

    return jsonify({'message': 'nothing found', 'data': {}})


@app.route('/addRuleEvent', methods=['POST'])
@jwt_required()
@swag_from('../../api_docs/Rule_Events/Post_Rule_Event.yml')
def post_rule_event():
    name_event = request.json['name_event']
    description = request.json['description']
    score = request.json['score']
    rule_description = request.json['rule_description']
    ruleevent = RuleEvents(name_event, description, score, rule_description)
    try:
        db.session.add(ruleevent)
        db.session.commit()
        result = ruleEvent_schema.dump(ruleevent)
        return jsonify({'message': 'successfully registered', 'data': result.data}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500


@app.route('/updateRuleEventId', methods=['PATH'])
@jwt_required()
@swag_from('../../api_docs/Rule_Events/Update_Rule_Event_Id.yml')
def update_rule_event_id(id):
    name_event = request.json['name_event']
    description = request.json['description']
    score = request.json['score']
    rule_description = request.json['rule_description']
    ruler_event = RuleEvents.query.get(id)

    if not ruler_event:
        return jsonify({'message': "Rule Event don't exist", 'data': {}}), 404
    if ruler_event:
        try:
            ruler_event.name_event = name_event
            ruler_event.description = description
            ruler_event.score = score
            ruler_event.rule_description = rule_description
            db.session.commit()
            result = ruleEvent_schema.dump(ruler_event)
            return jsonify({'message': 'successfully updated', 'data': result.data}), 201
        except:
            return jsonify({'message': 'unable to update', 'data': {}}), 500


@app.route('/deleteRuleEventId', methods=['DELETE'])
@jwt_required()
@swag_from('../../api_docs/Rule_Events/Delete_Rule_Event_Id.yml')
def delete_rule_event_id(id):
    rule_event = RuleEvents.query.get(id)
    if not rule_event:
        return jsonify({'message': "Rule Event don't exist", 'data': {}}), 404

    if rule_event:
        try:
            db.session.delete(rule_event)
            db.session.commit()
            result = ruleEvent_schema.dump(rule_event)
            return jsonify({'message': 'successfully deleted', 'data': result.data}), 200
        except:
            return jsonify({'message': 'unable to delete', 'data': {}}), 500


@app.route('/getRuleEventId', methods=['GET'])
@jwt_required()
@swag_from('../../api_docs/Rule_Events/Get_Rule_Event_Id.yml')
def get_rule_event_id(id):
    rule_event = RuleEvents.query.get(id)
    if rule_event:
        result = ruleEvent_schema.dump(rule_event)
        return jsonify({'message': 'successfully fetched', 'data': result.data}), 201

    return jsonify({'message': "user don't exist", 'data': {}}), 404
