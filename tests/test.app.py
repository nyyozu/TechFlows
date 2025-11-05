import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app as flask_app

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client

def test_login_valido(client):
    response = client.post('/', data={
        'usuario': 'admin',
        'senha': '1234'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Login realizado com sucesso!' in response.data

def test_login_invalido(client):
    response = client.post('/', data={
        'usuario': 'errado',
        'senha': 'errada'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Usuario ou senha invalidos.' in response.data