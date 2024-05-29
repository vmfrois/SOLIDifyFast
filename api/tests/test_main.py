from http import HTTPStatus

from fastapi.testclient import TestClient

from api.main import app


def test_read_root_should_return_ok():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert


def test_read_root_should_return_hello_world():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.json() == {'message': 'Hello world!'}  # Assert
