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


def test_insert_user_return_created():
    client = TestClient(app)  # Arrange

    response = client.post(  # Act
        '/users/',
        json={
            'username': 'string',
            'email': 'string@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED  # Assert


def test_insert_user_return_json():
    client = TestClient(app)  # Arrange

    response = client.post(  # Act
        '/users/',
        json={
            'username': 'string',
            'email': 'string@example.com',
            'password': 'secret',
        },
    )

    assert response.json() == {  # Assert
        'id': 2,
        'username': 'string',
        'email': 'string@example.com',
    }


def test_get_all_users():
    client = TestClient(app)  # Arrange

    response = client.get('/users/')  # Act

    assert response.json() == {  # Assert
        'users': [
            {
                'email': 'string@example.com',
                'id': 1,
                'username': 'string',
            },
            {
                'email': 'string@example.com',
                'id': 2,
                'username': 'string',
            },
        ]
    }


def test_get_user_by_id():
    client = TestClient(app)  # Arrange

    response = client.get('/users/1')  # Act

    assert response.json() == {
        'email': 'string@example.com',
        'id': 1,
        'username': 'string',
    }


def test_get_user_by_id_should_return_raise_exeception():
    client = TestClient(app)  # Arrange

    response = client.get('/users/0')  # Act

    assert response.json() == {
        'detail': 'User not found',
    }


def test_update_user_return_ok():
    client = TestClient(app)  # Arrange

    response = client.put(  # Act
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == HTTPStatus.OK  # Assert


def test_update_user_return_json():
    client = TestClient(app)  # Arrange

    response = client.put(  # Act
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.json() == {  # Assert
        'id': 1,
        'username': 'bob',
        'email': 'bob@example.com',
    }


def test_update_user_should_return_raise_exeception():
    client = TestClient(app)  # Arrange

    response = client.put(  # Act
        '/users/0',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.json() == {
        'detail': 'User not found',
    }


def test_delete_user():
    client = TestClient(app)  # Arrange

    response = client.delete('/users/1')  # Act

    assert response.json() == {'message': 'User deleted'}  # Assert


def test_delete_user_return_ok():
    client = TestClient(app)  # Arrange

    response = client.delete('/users/1')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert


def test_delete_users_hould_return_raise_exeception():
    client = TestClient(app)  # Arrange

    response = client.delete('/users/0')  # Act

    assert response.json() == {
        'detail': 'User not found',
    }
