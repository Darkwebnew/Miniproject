import io
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_upload_no_file(client):
    client.post('/login', data={'username':'heart123','password':'heart123'})
    assert client.post('/predict', data={}).status_code == 302
