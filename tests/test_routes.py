import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    assert client.get('/').status_code == 200

def test_login_success(client):
    response = client.post('/login', data={'username':'heart123','password':'heart123'}, follow_redirects=True)
    assert response.status_code == 200
