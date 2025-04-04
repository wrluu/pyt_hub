import pytest
from transaction_processor import search_operations_by_description, count_operations_by_category

def test_search_operations_by_description():
    transactions = [
        {'description': 'Открытие вклада'},
        {'description': 'Перевод с карты на карту'},
        {'description': 'Перевод организации'},
    ]
    result = search_operations_by_description(transactions, 'Перевод')
    assert result == [
        {'description': 'Перевод с карты на карту'},
        {'description': 'Перевод организации'},
    ]

def test_count_operations_by_category():
    transactions = [
        {'description': 'Открытие вклада'},
        {'description': 'Перевод с карты на карту'},
        {'description': 'Перевод организации'},
        {'description': 'Перевод с карты на карту'},
    ]
    categories = ['Открытие вклада', 'Перевод с карты на карту']
    result = count_operations_by_category(transactions, categories)
    assert result == {
        'Открытие вклада': 1,
        'Перевод с карты на карту': 2,
    }