from app import *
from unittest.mock import MagicMock, patch
import pytest

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@patch("app.validar_campos")
@patch("app.calcular_valor")
@patch("app.criar_objeto_movimentacao")
def test_criar_movimentacao_ok(client):
    resp = client.post("/movimentacoes")
    