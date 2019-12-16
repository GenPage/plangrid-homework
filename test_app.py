from app import app
import pytest


@pytest.fixture(scope='module')
def test_client():
    flask_app = app

    # https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.test_client
    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


def test_get(test_client):
    response = test_client.get("/hello")
    assert response.status_code == 200
    assert b'<p>Hello, World</p>' == response.data


def test_post(test_client):
    response = test_client.post("/hello")
    assert response.status_code == 200
    assert b'<p>Hello, World</p>' == response.data


def test_get_json(test_client):
    response = test_client.get("/hello", headers={"Accept": "application/json"})
    assert response.status_code == 200
    json_data = response.json
    assert json_data['message'] == "Hello, World!"


def test_post_json(test_client):
    response = test_client.post("/hello", headers={"Accept": "application/json"})
    assert response.status_code == 200
    json_data = response.json
    assert json_data['message'] == "Hello, World!"