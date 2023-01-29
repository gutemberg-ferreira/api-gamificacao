from flask import jsonify, request
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from sqlalchemy import desc
from api.models.listen_events import LISTENEVENTS
from app import app, db


@app.route('/rankingAll', methods=['GET'])
@jwt_required()
@swag_from('../../api_docs/Rank/Get_Ranking_All.yml')
def get_ranking_all():
    nameListenEvent = request.args.get('nameListenEvent')
    if nameListenEvent:
        listen_event = LISTENEVENTS.query.filter(LISTENEVENTS.name.like(f'%{nameListenEvent}%')).all()
    else:
        query = db.select([LISTENEVENTS.user_id, db.func.sum(LISTENEVENTS.generated_score).label('Overall_Score')]).order_by(desc('Overall_Score')).group_by(LISTENEVENTS.user_id)
        listen_event = db.engine.execute(query).fetchall()
    if listen_event:
        return jsonify({'message': 'successfully fetched', 'data': [dict(row) for row in listen_event]})
    return jsonify({'message': 'OK', 'data': {}})


@app.route('/userScoreByCommunity/<int:id>', methods=['GET'])
@jwt_required()
@swag_from('../../api_docs/Rank/Get_User_Score_by_Community.yml')
def get_user_score_bycommunity(id):
    nameListenEvent = request.args.get('nameListenEvent')
    if nameListenEvent:
        listen_event = LISTENEVENTS.query.filter(LISTENEVENTS.name.like(f'%{nameListenEvent}%')).all()
    else:
        query = db.select([LISTENEVENTS.community_id, LISTENEVENTS.user_id, db.func.sum(LISTENEVENTS.generated_score).label('Overall_Score')]).where(LISTENEVENTS.user_id==id).order_by(desc('Overall_Score')).group_by(LISTENEVENTS.community_id)
        listen_event = db.engine.execute(query).fetchall()
    if listen_event:
        return jsonify({'message': 'successfully fetched', 'data': [dict(row) for row in listen_event]})
    return jsonify({'message': 'OK', 'data': {}})


@app.route('/userScoreTotal/<int:id>', methods=['GET'])
@jwt_required()
@swag_from('../../api_docs/Rank/Get_User_Score_Total.yml')
def get_user_score_total(id):
    nameListenEvent = request.args.get('nameListenEvent')
    if nameListenEvent:
        listen_event = LISTENEVENTS.query.filter(LISTENEVENTS.name.like(f'%{nameListenEvent}%')).all()
    else:
        query = db.select([LISTENEVENTS.user_id, db.func.sum(LISTENEVENTS.generated_score).label('Overall_Score')]).where(LISTENEVENTS.user_id == id).group_by(LISTENEVENTS.user_id)
        listen_event = db.engine.execute(query).fetchall()
    if listen_event:
        return jsonify({'message': 'successfully fetched', 'data': [dict(row) for row in listen_event]})
    return jsonify({'message': 'OK', 'data': {}})


@app.route('/ScoreByCommunity/<int:id>', methods=['GET'])
@jwt_required()
@swag_from('../../api_docs/Rank/Get_Score_by_Community.yml')
def get_user_score_by_community(id):
    nameListenEvent = request.args.get('nameListenEvent')
    if nameListenEvent:
        listen_event = LISTENEVENTS.query.filter(LISTENEVENTS.name.like(f'%{nameListenEvent}%')).all()
    else:
        query = db.select([LISTENEVENTS.community_id, LISTENEVENTS.user_id, db.func.sum(LISTENEVENTS.generated_score).label('Overall_Score')]).where(LISTENEVENTS.community_id==id).order_by(desc('Overall_Score')).group_by(LISTENEVENTS.user_id)
        listen_event = db.engine.execute(query).fetchall()
    if listen_event:
        return jsonify({'message': 'successfully fetched', 'data': [dict(row) for row in listen_event]})
    return jsonify({'message': 'OK', 'data': {}})