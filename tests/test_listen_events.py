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


def test_get_all_listen_events(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    response = client.get('/allListen', headers=dict(Authorization=token))
    assert response.status_code == 200


def test_post_listen_event(app, client):
    listen_event = {
                        'user_id': 1,
                        'event_date': '2023-01-28 00:10:00',
                        'community_id': 1,
                        'event_id': 1
    }
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.post('/addListenEvent', headers=header, data=json.dumps(listen_event))
    global id
    id = response.json['data']['id']
    assert response.status_code == 201


def test_update_listen_event_id(app, client):
    listen_event = {
                        'user_id': 1,
                        'event_date': '2023-01-28 00:10:00',
                        'community_id': 1,
                        'event_id': 1
    }
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.patch('/updateListenEventId/' + str(id), headers=header, data=json.dumps(listen_event))
    assert response.status_code == 201


def test_update_listen_event_id_404(app, client):
    listen_event = {
                        'user_id': 1,
                        'event_date': '2023-01-28 00:10:00',
                        'community_id': 1,
                        'event_id': 1
    }
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.patch('/updateListenEventId/0', headers=header, data=json.dumps(listen_event))
    assert response.status_code == 404


def test_get_listen_event_id(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.get('/getListenEventId/' + str(id), headers=header)
    assert response.status_code == 200


def test_get_listen_event_id_404(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.get('/getListenEventId/0', headers=header)
    assert response.status_code == 404



def test_delete_listen_event_id(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.delete('/deleteListenEventId/' + str(id), headers=header)
    assert response.status_code == 200


def test_delete_listen_event_id_404(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.delete('/deleteListenEventId/0', headers=header)
    assert response.status_code == 404
