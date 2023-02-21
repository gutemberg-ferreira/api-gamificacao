# coding: utf-8

import pytest
from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.mark.app_test
def test_index(app, client):
    response = client.get('/')
    assert response.status_code == 200

