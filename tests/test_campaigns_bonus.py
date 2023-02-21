# coding: utf-8

import pytest
import json
from app import app as flask_app


id = None


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_all_campaigns_bonus(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    response = client.get('/allCampaignsBonus', headers=dict(Authorization=token))
    assert response.status_code == 200


def test_post_campaigns_bonus(app, client):
    campaig_bonus = {
                        'name': 'Test',
                        'date_begin': '2023-01-28 00:10:00',
                        'date_end': '2023-01-28 00:10:00',
                        'bonus': '1.5',
                        'community_id': 1,
                        'event_ids': '1',
                        'status': True
    }
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.post('/addCampaignsBonus', headers=header, data=json.dumps(campaig_bonus))
    global id
    id = response.json['data']['id']
    assert response.status_code == 201


def test_update_campaigns_bonus_id(app, client):
    campaig_bonus_edit = {
                        'name': 'Test',
                        'date_begin': '2023-01-28 00:10:00',
                        'date_end': '2023-01-28 00:10:00',
                        'bonus': '1.5',
                        'community_id': 1,
                        'event_ids': '1',
                        'status': True
    }
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.patch('/updateCampaignsBonusId/' + str(id), headers=header, data=json.dumps(campaig_bonus_edit))
    assert response.status_code == 201

def test_update_campaigns_bonus_id_404(app, client):
    campaig_bonus_edit = {
                        'name': 'Test',
                        'date_begin': '2023-01-28 00:10:00',
                        'date_end': '2023-01-28 00:10:00',
                        'bonus': '1.5',
                        'community_id': 1,
                        'event_ids': '1',
                        'status': True
    }
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.patch('/updateCampaignsBonusId/0', headers=header, data=json.dumps(campaig_bonus_edit))
    assert response.status_code == 404


def test_get_campaigns_bonus_id(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.get('/getCampaignsBonusId/' + str(id), headers=header)
    assert response.status_code == 200


def test_get_campaigns_bonus_id_404(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.get('/getCampaignsBonusId/0', headers=header)
    assert response.status_code == 404



def test_delete_campaigns_bonus_event_id(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.delete('/deleteCampaignsBonusId/' + str(id), headers=header)
    assert response.status_code == 200


def test_delete_campaigns_bonus_event_id_404(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.delete('/deleteCampaignsBonusId/0', headers=header)
    assert response.status_code == 404
