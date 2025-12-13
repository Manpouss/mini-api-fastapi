import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.routes.tasks import fake_tasks_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_db():
    # avant chaque test
    fake_tasks_db.clear()
    yield
    # après chaque test (par sécurité)
    fake_tasks_db.clear()

def test_create_task():
    r = client.post("/tasks/", json={"title": "t1", "description": "d1"})
    assert r.status_code == 201
    data = r.json()
    assert data["id"] == 1
    assert data["title"] == "t1"
    assert data["description"] == "d1"
    assert data["done"] is False

def test_list_tasks():
    client.post("/tasks/", json={"title": "t1"})
    client.post("/tasks/", json={"title": "t2"})
    r = client.get("/tasks/")
    assert r.status_code == 200
    data = r.json()
    assert len(data) == 2
    assert data[0]["id"] == 1
    assert data[1]["id"] == 2

def test_get_by_id_found():
    client.post("/tasks/", json={"title": "t1"})
    r = client.get("/tasks/1")
    assert r.status_code == 200
    assert r.json()["title"] == "t1"

def test_get_by_id_not_found():
    r = client.get("/tasks/999")
    assert r.status_code == 404
    assert r.json()["detail"] == "Task not found"

def test_update_by_id():
    client.post("/tasks/", json={"title": "t1", "description": "d1"})
    r = client.put("/tasks/1", json={"title": "t1-updated", "done": True})
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == 1
    assert data["title"] == "t1-updated"
    assert data["description"] == "d1"  # inchangé
    assert data["done"] is True

def test_delete_by_id():
    client.post("/tasks/", json={"title": "t1"})
    r = client.delete("/tasks/1")
    assert r.status_code == 204
    r2 = client.get("/tasks/")
    assert r2.status_code == 200
    assert r2.json() == []

def test_delete_all():
    client.post("/tasks/", json={"title": "t1"})
    client.post("/tasks/", json={"title": "t2"})
    r = client.delete("/tasks/")
    assert r.status_code == 204
    r2 = client.get("/tasks/")
    assert r2.json() == []
