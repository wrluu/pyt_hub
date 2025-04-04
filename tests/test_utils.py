from unittest.mock import mock_open, patch

import pytest

from src.utils import read_json


@pytest.fixture
def mock_json_file():
    return '[{"amount": 100, "currency": "USD"}, {"amount": 200, "currency": "EUR"}]'

def test_read_json_success(mock_json_file):
    with patch('builtins.open', new_callable=mock_open, read_data=mock_json_file):
        result = read_json('fake_path.json')
        expected_result = [{"amount": 100, "currency": "USD"}, {"amount": 200, "currency": "EUR"}]
        print(result)
        assert result == expected_result

def test_read_json_file_not_found():
    with patch('builtins.open', side_effect=FileNotFoundError()):
        result = read_json('fake_path.json')
        assert result == []

def test_read_json_not_a_list():
    with patch('builtins.open', new_callable=mock_open, read_data='not_a_list'):
        result = read_json('fake_path.json')
        assert result == []