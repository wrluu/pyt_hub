import pytest
from datetime import datetime
from processing import (filter_by_state, sort_by_date)

@pytest.fixture
def sample_data():
    return [
        {"state": "EXECUTED", "date": "2024-03-11T02:26:18.671407"},
        {"state": "PENDING", "date": "2024-03-10T02:26:18.671407"},
        {"state": "EXECUTED", "date": "2024-03-09T02:26:18.671407"},
        {"state": "CANCELLED", "date": "2024-03-08T02:26:18.671407"},
    ]

def test_filter_by_state(sample_data):
    result = filter_by_state(sample_data, state='EXECUTED')
    assert len(result) == 2
    assert all(item['state'] == 'EXECUTED' for item in result)

def test_filter_by_state_no_match(sample_data):
    result = filter_by_state(sample_data, state='FAILED')
    assert len(result) == 0

@pytest.mark.parametrize("descending, expected_order", [
    (True, ["2024-03-11T02:26:18.671407", "2024-03-10T02:26:18.671407", "2024-03-09T02:26:18.671407", "2024-03-08T02:26:18.671407"]),
    (False, ["2024-03-08T02:26:18.671407", "2024-03-09T02:26:18.671407", "2024-03-10T02:26:18.671407", "2024-03-11T02:26:18.671407"]),
])
def test_sort_by_date(sample_data, descending, expected_order):
    result = sort_by_date(sample_data, descending=descending)
    assert [item['date'] for item in result] == expected_order