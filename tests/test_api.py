import os
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

os.environ.setdefault('DATABASE_URL', 'sqlite:///./test_todos.db')

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def test_health_check():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}


def test_create_and_list_todos():
    response = client.post('/api/todos', json={'title': '테스트 할 일'})
    assert response.status_code == 201
    payload = response.json()
    assert payload['title'] == '테스트 할 일'
    assert payload['completed'] is False

    list_response = client.get('/api/todos')
    assert list_response.status_code == 200
    assert any(item['title'] == '테스트 할 일' for item in list_response.json())


def test_reject_empty_title():
    response = client.post('/api/todos', json={'title': '   '})
    assert response.status_code == 422


def test_serves_static_assets():
    styles_response = client.get('/static/styles.css')
    assert styles_response.status_code == 200
    assert 'body' in styles_response.text

    app_js_response = client.get('/static/app.js')
    assert app_js_response.status_code == 200
    assert 'toggleTodo' in app_js_response.text


def test_toggle_and_delete_todo():
    created = client.post('/api/todos', json={'title': '완료 테스트'}).json()
    toggle_response = client.patch(f"/api/todos/{created['id']}", json={'completed': True})
    assert toggle_response.status_code == 200
    assert toggle_response.json()['completed'] is True

    delete_response = client.delete(f"/api/todos/{created['id']}")
    assert delete_response.status_code == 204

    missing_response = client.delete(f"/api/todos/{created['id']}")
    assert missing_response.status_code == 404
