from unittest.mock import patch
import pytest
from src.external_api import convert_currency

def test_convert_currency_usd():
    with patch('src.external_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'rates': {'RUB': 75.0}}

        transaction = {'operationAmount': {'amount': '100', 'currency': {'code': 'USD'}}}
        result = convert_currency(transaction)
        assert result == 7500.0

def test_convert_currency_rub():
    transaction = {'operationAmount': {'amount': '300', 'currency': {'code': 'RUB'}}}
    result = convert_currency(transaction)
    assert result == 300.0
