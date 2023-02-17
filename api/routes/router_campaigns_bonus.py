from flask import jsonify, request
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from api.models.campaigns_bonus import CAMPAIGNSBONUS, CampaignsBonus_schema, CampaignsBonusS_schema
from app import app, db


@app.route('/addCampaignsBonus', methods=['POST'])
@swag_from('../../api_docs/Campaigns_Bonus/Post_Campaigns_Bonus.yml')
def post_campaigns_bonus():
    id = None
    name = request.json['name']
    date_begin = request.json['date_begin']
    date_end = request.json['date_end']
    bonus = request.json['bonus']
    community_id = request.json['community_id']
    event_ids = request.json['event_ids']
    status = request.json['status']
    campaigns = CAMPAIGNSBONUS(id, name, date_begin, date_end, bonus, community_id, event_ids, status)

    try:
        db.session.add(campaigns)
        db.session.commit()
        result = CampaignsBonus_schema.dump(campaigns)
        return jsonify({'message': 'successfully registered', 'data': result.data}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500


@app.route('/updateCampaignsBonusId/<int:id>', methods=['PATCH'])
@jwt_required()
@swag_from('../../api_docs/Campaigns_Bonus/Update_Campaigns_Bonus_Id.yml')
def update_campaigns_bonus_id(id):
    name = request.json['name']
    date_begin = request.json['date_begin']
    date_end = request.json['date_end']
    bonus = request.json['bonus']
    community_id = request.json['community_id']
    event_ids = request.json['event_ids']
    status = request.json['status']
    campaigns_bonus = CAMPAIGNSBONUS.query.get(id)

    if not campaigns_bonus:
        return jsonify({'message': "Rule Event don't exist", 'data': {}}), 404
    if campaigns_bonus:
        try:
            campaigns_bonus.name = name
            campaigns_bonus.date_begin = date_begin
            campaigns_bonus.date_end = date_end
            campaigns_bonus.bonus = bonus
            campaigns_bonus.community_id = community_id
            campaigns_bonus.event_ids = event_ids
            campaigns_bonus.status = status
            db.session.commit()
            result = CampaignsBonus_schema.dump(campaigns_bonus)
            return jsonify({'message': 'successfully updated', 'data': result.data}), 201
        except:
            return jsonify({'message': 'unable to update', 'data': {}}), 500


@app.route('/allCampaignsBonus', methods=['GET'])
@jwt_required()
@swag_from('../../api_docs/Campaigns_Bonus/Get_All_Campaigns_Bonus.yml')
def get_all_campaigns_bonus():
    nameEvent = request.args.get('nameEvent')
    if nameEvent:
        event = CAMPAIGNSBONUS.query.filter(CAMPAIGNSBONUS.name.like(f'%{nameEvent}%')).all()
    else:
        event = CAMPAIGNSBONUS.query.all()
    if event:
        result = CampaignsBonusS_schema.dump(event)
        return jsonify({'message': 'successfully fetched', 'data': result.data})

    return jsonify({'message': 'nothing found', 'data': {}})


@app.route('/deleteCampaignsBonusId/<int:id>', methods=['DELETE'])
@jwt_required()
@swag_from('../../api_docs/Campaigns_Bonus/Delete_CampaignsBonus_Id.yml')
def delete_campaigns_bonus_event_id(id):
    campaigns_bonus = CAMPAIGNSBONUS.query.get(id)
    if not campaigns_bonus:
        return jsonify({'message': "Rule Event don't exist", 'data': {}}), 404

    if campaigns_bonus:
        try:
            db.session.delete(campaigns_bonus)
            db.session.commit()
            return jsonify({'message': 'successfully deleted'}), 200
        except:
            return jsonify({'message': 'unable to delete', 'data': {}}), 500


@app.route('/getCampaignsBonusId/<int:id>', methods=['GET'])
@jwt_required()
@swag_from('../../api_docs/Campaigns_Bonus/Get_CampaignsBonus_Id.yml')
def get_campaigns_bonus_id(id):
    campaigns_bonus = CAMPAIGNSBONUS.query.get(id)
    if campaigns_bonus:
        result = CampaignsBonus_schema.dump(campaigns_bonus)
        return jsonify({'message': 'successfully fetched', 'data': result.data}), 200

    return jsonify({'message': "user don't exist", 'data': {}}), 404