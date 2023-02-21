# coding: utf-8

import pytest

from api.models.campaigns_bonus import CAMPAIGNSBONUS
from api.models.rule_events import RULEEVENTS
from api.models.users import USERS
from app import app as flask_app
from flask_login import FlaskLoginClient
from faker import Faker

id = None


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_dash_rank(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    with app.test_client(user=user) as client:
        response = client.get('/dashrank')
    assert response.status_code == 200


def test_get_rule_events_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    with app.test_client(user=user) as client:
        response = client.get('/admin/ruleevents')
    assert response.status_code == 200


def test_get_campaigns_bonus_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    with app.test_client(user=user) as client:
        response = client.get('/admin/campaignsbonus')
    assert response.status_code == 200


def test_get_users_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    with app.test_client(user=user) as client:
        response = client.get('/admin/users')
    assert response.status_code == 200


def test_post_rule_events_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    rule_event = {
                        'name_event': 'Event Test',
                        'description': 'Description Event Test',
                        'score': 1000,
                        'rule_description': 'Rule Description Event Test',
                        'status': True
    }
    with app.test_client(user=user) as client:
        response = client.post('/admin/addRuleEventHtml', data=rule_event)

    query = RULEEVENTS.query.all()
    last_item = query[-1]
    global id
    id = last_item.id
    assert response.status_code == 302


def test_update_rule_events_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    rule_event = {
                        'name_event': 'Event Test Editado',
                        'description': 'Description Event Test Editado',
                        'score': 1000,
                        'rule_description': 'Rule Description Event Test Editado',
                        'status': True
    }
    with app.test_client(user=user) as client:
        response = client.post('/admin/ruleevents/'+ str(id) +'/update', data=rule_event)
    assert response.status_code == 302


def test_get_update_rule_events_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    with app.test_client(user=user) as client:
        response = client.get('/admin/ruleevents/' + str(id) + '/update')
    assert response.status_code == 200


def test_get_rule_events_delete_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    with app.test_client(user=user) as client:
        response = client.get('/admin/ruleevents/' + str(id) + '/delete')
    assert response.status_code == 200


def test_rule_events_delete_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    with app.test_client(user=user) as client:
        response = client.post('/admin/ruleevents/' + str(id) + '/delete')
    assert response.status_code == 302


def test_post_campaigns_bonus_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    campaig_bonus = {
                        'name': 'Test',
                        'date_begin': '2023-01-28 00:10:00',
                        'date_end': '2023-01-28 00:10:00',
                        'bonus': '1.5',
                        'community_id': 1,
                        'event_ids': '1',
                        'status': True
    }
    with app.test_client(user=user) as client:
        response = client.post('/admin/addCampaignsBonusHtml', data=campaig_bonus)
    query = CAMPAIGNSBONUS.query.all()
    last_item = query[-1]
    global id
    id = last_item.id
    assert response.status_code == 302


def test_campaigns_bonus_update_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    campaig_bonus = {
                        'name': 'Test Editado',
                        'date_begin': '2023-01-28 00:10:00',
                        'date_end': '2023-01-28 00:10:00',
                        'bonus': '1.5',
                        'community_id': 1,
                        'event_ids': '1',
                        'status': True
    }
    with app.test_client(user=user) as client:
        response = client.post('/admin/campaignsbonus/' + str(id) + '/update', data=campaig_bonus)
    assert response.status_code == 302


def test_get_update_campaigns_bonus_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    with app.test_client(user=user) as client:
        response = client.get('/admin/campaignsbonus/' + str(id) + '/update')
    assert response.status_code == 200


def test_get_campaigns_bonus_delete_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    with app.test_client(user=user) as client:
        response = client.get('/admin/campaignsbonus/' + str(id) + '/delete')
    assert response.status_code == 200


def test_campaigns_bonus_delete_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    with app.test_client(user=user) as client:
        response = client.post('/admin/campaignsbonus/' + str(id) + '/delete')
    assert response.status_code == 302


def test_post_users_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    fake = Faker('pt_BR')
    useradd = {
                        'username': fake.first_name(),
                        'password': 'test123',
                        'name': fake.name(),
                        'email': fake.email()
    }
    with app.test_client(user=user) as client:
        response = client.post('/admin/addUsersHtml', data=useradd)
    query = USERS.query.all()
    last_item = query[-1]
    global id
    id = last_item.id
    assert response.status_code == 302


def test_users_update_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    useradd = {
                        'username': 'TestEditado',
                        'password': 'test123',
                        'name': 'Name Editado',
                        'email': 'Email@Editado.com'
    }
    with app.test_client(user=user) as client:
        response = client.post('/admin/users/' + str(id) + '/update', data=useradd)
    assert response.status_code == 302


def test_get_users_update_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    with app.test_client(user=user) as client:
        response = client.get('/admin/users/' + str(id) + '/update')
    assert response.status_code == 200


def test_post_users_change_pass_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    userpass = {
                        'password': 'test123',
    }
    with app.test_client(user=user) as client:
        response = client.post('/admin/users/' + str(id) + '/changepass', data=userpass)
    assert response.status_code == 302


def test_get_users_change_pass_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    with app.test_client(user=user) as client:
        response = client.get('/admin/users/' + str(id) + '/changepass')
    assert response.status_code == 200


def test_get_users_delete_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    with app.test_client(user=user) as client:
        response = client.get('/admin/users/' + str(id) + '/delete')
    assert response.status_code == 200


def test_users_delete_html(app, client):
    app.test_client_class = FlaskLoginClient
    user = USERS.query.get(1)
    with app.test_client(user=user) as client:
        response = client.post('/admin/users/' + str(id) + '/delete')
    assert response.status_code == 302


