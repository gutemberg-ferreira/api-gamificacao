# coding: utf-8

import pytest
import json
from faker import Faker

from app import app as flask_app


id = None


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_users(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    response = client.get('/all', headers=dict(Authorization=token))
    assert response.status_code == 200


def test_post_user(app, client):
    fake = Faker('pt_BR')

    user = {
                        'username': fake.first_name(),
                        'password': 'test123',
                        'name': fake.name(),
                        'email': fake.email()
    }
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.post('/addUser', headers=header, data=json.dumps(user))
    global id
    id = response.json['data']['id']
    assert response.status_code == 201


def test_update_user(app, client):
    fake = Faker('pt_BR')
    user = {
                        'username': fake.first_name(),
                        'password': 'test123',
                        'name': fake.name(),
                        'email': fake.email()
    }
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.patch('/updateUserID/' + str(id), headers=header, data=json.dumps(user))
    assert response.status_code == 201

def test_update_user_404(app, client):
    fake = Faker('pt_BR')
    user = {
                        'username': fake.name() + 'test',
                        'password': 'test123',
                        'name': fake.name(),
                        'email': fake.email()
    }
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.patch('/updateUserID/0', headers=header, data=json.dumps(user))
    assert response.status_code == 404


def test_get_user(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.get('/getUserID/' + str(id), headers=header)
    assert response.status_code == 200


def test_get_user_404(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.get('/getUserID/0', headers=header)
    assert response.status_code == 404



def test_delete_user(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.delete('/deleteUserID/' + str(id), headers=header)
    assert response.status_code == 200


def test_delete_user_404(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    header = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = client.delete('/deleteUserID/0', headers=header)
    assert response.status_code == 404
