# coding: utf-8

import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_ranking_all(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    response = client.get('/rankingAll', headers=dict(Authorization=token))
    assert response.status_code == 200


def test_ranking_user_score_by_community(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    response = client.get('/userScoreByCommunity/1', headers=dict(Authorization=token))
    assert response.status_code == 200


def test_ranking_user_score_total(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    response = client.get('/userScoreTotal/1', headers=dict(Authorization=token))
    assert response.status_code == 200


def test_ranking_score_by_community(app, client):
    auth = client.post('/auth', headers=dict(username='test', password='test123'))
    token = auth.json['token']
    response = client.get('/ScoreByCommunity/1', headers=dict(Authorization=token))
    assert response.status_code == 200
