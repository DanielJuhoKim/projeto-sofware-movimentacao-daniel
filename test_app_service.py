from app_service import *
from unittest.mock import MagicMock, patch
data = {
        "cpf_comprador": "123",
        "cpf_vendedor": "456",
        "ticker": "PETR4",
        "quantidade": 10,
        "lastValue": 70
    }

def test_validar_campos_completos():

    assert validar_campos(data) is None

@patch("app_service.requests.get")
def test_calcular_valor_correto(mock_get):
    mock_resposta = MagicMock()
    mock_resposta.status_code = 200
    mock_resposta.json() == data
    mock_get.return_value = mock_resposta

    valor, erro = calcular_valor(data["ticker"], data["quantidade"])

    assert valor != None
    assert erro is None

def test_criar_objeto_movimentacao():
    valor_total = data["quantidade"] * data["lastValue"]

    objeto = {
        "cpf_comprador": data["cpf_comprador"],
        "cpf_vendedor": data["cpf_vendedor"],
        "ticker": data["ticker"],
        "quantidade": data["quantidade"],
        "valor_movimentacao": valor_total
    }

    assert objeto == criar_objeto_movimentacao(data, valor_total)
