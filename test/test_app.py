import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_sumar(client):
    response = client.get('/sumar?a=5&b=3')
    assert response.status_code == 200
    assert response.json == {"resultado": 8}

def test_dividir_por_cero(client):
    response = client.get('/dividir?a=10&b=0')
    assert response.status_code == 400
    assert response.json == {"error": "No se puede dividir entre 0"}