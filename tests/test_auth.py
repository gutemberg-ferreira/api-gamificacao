# coding: utf-8

import pytest
from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_login(app, client):
    response = client.get('/login')
    assert response.status_code == 200


def test_post_login(app, client):
    user = {
                        'HTTP_USERNAME': 'test',
                        'HTTP_PASSWORD': 'test123',
                        'REMEMBER': True
    }
    response = client.post('/login', data=user)
    assert response.status_code == 302


def test_post_login_pass_bad(app, client):
    user = {
                        'HTTP_USERNAME': 'test',
                        'HTTP_PASSWORD': 'test1234',
                        'REMEMBER': True
    }
    response = client.post('/login', data=user)
    assert response.status_code == 302


def test_get_logout(app, client):
    response = client.get('/logout')
    assert response.status_code == 302






