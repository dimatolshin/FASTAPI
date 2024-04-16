from main import app
from MAIN.SQLAlchemi.database import *
from fastapi.testclient import TestClient

Base.metadata.create_all(bind=engine)
client = TestClient(app)
person = db.query(Person).filter(Person.name == 'nika').first()


def test_read_main():
    response = client.get("/api/users")
    assert response.status_code == 200
    assert response.json() == [{'age': user.age, 'id': user.id, 'name': user.name} for user in db.query(Person).all()]


def test_create_user():
    response = client.post(
        "/api/users",
        json={'name': 'nika', 'age': 21})
    assert response.status_code == 200
    user = db.query(Person).filter(Person.name == 'nika').first()
    assert response.json() == {'id': user.id, 'name': user.name, 'age': user.age}


def test_delete_user():
    response = client.delete(f"/api/users/{person.id}")
    assert response.status_code == 200
    assert response.json() == {'id': person.id, 'name': person.name, 'age': person.age}


def test_get_user():
    response = client.get(f"/api/users/{person.id}")
    assert response.status_code == 200
    assert response.json() == {'id': person.id, 'name': person.name, 'age': person.age}
