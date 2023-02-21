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


def test_get_all_rule_events(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    response = client.get('/allEvents', headers=dict(Authorization=token))
    assert response.status_code == 200


def test_post_rule_event(app, client):
    rule_event = {
                        'name_event': 'Event Test',
                        'description': 'Description Event Test',
                        'score': 1000,
                        'rule_description': 'Rule Description Event Test',
                        'status': True
    }
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.post('/addRuleEvent', headers=header, data=json.dumps(rule_event))
    global id
    id = response.json['data']['id']
    assert response.status_code == 201


def test_update_rule_event_id(app, client):
    rule_event = {
                        'name_event': 'Event Test Edit',
                        'description': 'Description Event Test Edit',
                        'score': 1000,
                        'rule_description': 'Rule Description Event Test Edit',
                        'status': True
    }
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.patch('/updateRuleEventId/' + str(id), headers=header, data=json.dumps(rule_event))
    assert response.status_code == 201

def test_update_rule_event_id_404(app, client):
    rule_event = {
                        'name_event': 'Event Test Edit',
                        'description': 'Description Event Test Edit',
                        'score': 1000,
                        'rule_description': 'Rule Description Event Test Edit',
                        'status': True
    }
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.patch('/updateRuleEventId/0', headers=header, data=json.dumps(rule_event))
    assert response.status_code == 404


def test_get_rule_event_id(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.get('/getRuleEventId/' + str(id), headers=header)
    assert response.status_code == 200


def test_get_rule_event_id_404(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.get('/getRuleEventId/0', headers=header)
    assert response.status_code == 404



def test_delete_rule_event_id(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.delete('/deleteRuleEventId/' + str(id), headers=header)
    assert response.status_code == 200


def test_delete_rule_event_id_404(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.delete('/deleteRuleEventId/0', headers=header)
    assert response.status_code == 404
