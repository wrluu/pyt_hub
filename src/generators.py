def filter_by_currency(transactions, currency_code):
    """
    Генератор, который фильтрует транзакции по заданной валюте.
    """
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction

def transaction_descriptions(transactions):
    """
    Генератор, который возвращает описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction['description']

def card_number_generator(start, end):
    """
    Генератор, который выдает номера банковских карт в заданном диапазоне.
    """
    for number in range(start, end + 1):
        yield f"{number:016}"