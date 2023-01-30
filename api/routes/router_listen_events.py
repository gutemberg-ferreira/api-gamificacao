from flask import jsonify, request
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from api.models.listen_events import LISTENEVENTS, listenEvent_schema, listenEvents_schema
from api.models.rule_events import RULEEVENTS
from app import app, db


@app.route('/allListen', methods=['GET'])
@jwt_required()
@swag_from('../../api_docs/Listen_Events/Get_All_Listen_Events.yml')
def get_all_listen_events():
    nameListenEvent = request.args.get('nameListenEvent')
    if nameListenEvent:
        listen_event = LISTENEVENTS.query.filter(LISTENEVENTS.name.like(f'%{nameListenEvent}%')).all()
    else:
        listen_event = LISTENEVENTS.query.all()
    if listen_event:
        result = listenEvents_schema.dump(listen_event)
        return jsonify({'message': 'successfully fetched', 'data': result.data})

    return jsonify({'message': 'nothing found', 'data': {}})


@app.route('/addListenEvent', methods=['POST'])
@jwt_required()
@swag_from('../../api_docs/Listen_Events/Post_Listen_Event.yml')
def post_listen_event():
    id = None
    user_id = request.json['user_id']
    event_date = request.json['event_date']
    community_id = request.json['community_id']
    event_id = request.json['event_id']
    query = RULEEVENTS.query.get(event_id)
    if query.status:
        # TODO verificação de campanha ativa
        generated_score = query.score
    else:
        generated_score = 0

    listenevents = LISTENEVENTS(id, user_id, event_date, community_id, event_id, generated_score)

    try:
        db.session.add(listenevents)
        db.session.commit()
        result = listenEvent_schema.dump(listenevents)
        return jsonify({'message': 'successfully registered', 'data': result.data}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500


@app.route('/updateListenEventId/<int:id>', methods=['PATCH'])
@jwt_required()
@swag_from('../../api_docs/Listen_Events/Update_Listen_Event_Id.yml')
def update_listen_event_id(id):
    user_id = request.json['user_id']
    event_date = request.json['event_date']
    community_id = request.json['community_id']
    event_id = request.json['event_id']
    listen_event = LISTENEVENTS.query.get(id)

    if not listen_event:
        return jsonify({'message': "Rule Event don't exist", 'data': {}}), 404
    if listen_event:
        try:
            listen_event.user_id = user_id
            listen_event.event_date = event_date
            listen_event.community_id = community_id
            listen_event.event_id = event_id
            db.session.commit()
            result = listenEvent_schema.dump(listen_event)
            return jsonify({'message': 'successfully updated', 'data': result.data}), 201
        except:
            return jsonify({'message': 'unable to update', 'data': {}}), 500


@app.route('/deleteListenEventId/<int:id>', methods=['DELETE'])
@jwt_required()
@swag_from('../../api_docs/Listen_Events/Delete_Listen_Event_Id.yml')
def delete_listen_event_id(id):
    listen_event = LISTENEVENTS.query.get(id)
    if not listen_event:
        return jsonify({'message': "Rule Event don't exist", 'data': {}}), 404

    if listen_event:
        try:
            db.session.delete(listen_event)
            db.session.commit()
            result = listenEvent_schema(listen_event)
            return jsonify({'message': 'successfully deleted', 'data': result.data}), 200
        except:
            return jsonify({'message': 'unable to delete', 'data': {}}), 500


@app.route('/getListenEventId/<int:id>', methods=['GET'])
@jwt_required()
@swag_from('../../api_docs/Listen_Events/Get_Listen_Event_Id.yml')
def get_listen_event_id(id):
    listen_event = LISTENEVENTS.query.get(id)
    if listen_event:
        result = listenEvent_schema.dump(listen_event)
        return jsonify({'message': 'successfully fetched', 'data': result.data}), 200

    return jsonify({'message': "user don't exist", 'data': {}}), 404