# test_generators.py

import pytest
from generators import filter_by_currency, transaction_descriptions, card_number_generator

transactions = [
    {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "Описание 1"},
    {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}, "description": "Описание 2"},
    {"id": 3, "operationAmount": {"currency": {"code": "USD"}}, "description": "Описание 3"},
]

def test_filter_by_currency():
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 2
    assert all(t['operationAmount']['currency']['code'] == "USD" for t in usd_transactions)

    eur_transactions = list(filter_by_currency(transactions, "EUR"))
    assert len(eur_transactions) == 1
    assert all(t['operationAmount']['currency']['code'] == "EUR" for t in eur_transactions)

    empty_transactions = list(filter_by_currency(transactions, "RUB"))
    assert len(empty_transactions) == 0

def test_transaction_descriptions():
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == ["Описание 1", "Описание 2", "Описание 3"]

    empty_descriptions = list(transaction_descriptions([]))
    assert empty_descriptions == []

def test_card_number_generator():
    card_numbers = list(card_number_generator(1, 3))
    assert card_numbers == ["0000000000000001", "0000000000000002", "0000000000000003"]

    single_card_number = list(card_number_generator(1, 1))
    assert single_card_number == ["0000000000000001"]

    empty_card_numbers = list(card_number_generator(2, 1))
    assert empty_card_numbers == []
