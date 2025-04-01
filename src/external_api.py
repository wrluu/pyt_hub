import os

import requests

API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")
BASE_URL = "http://api.exchangeratesapi.io/v1/latest?access_key={}&base=USD".format(API_KEY)


def convert_currency(amount, currency):
    """
    Функция для конвертации валюты в рубли.
    """
    if currency == 'RUB':
        return amount

    response = requests.get(BASE_URL)
    rates = response.json().get('rates', {})

    if currency == 'USD':
        rate = rates.get('RUB', 1.0)  # Используем 1.0 по умолчанию, если курс не найден
    elif currency == 'EUR':
        rub_rate = rates.get('RUB', 1.0)
        eur_rate = rates.get('EUR', 1.0)
        rate = rub_rate / eur_rate
    else:
        raise ValueError(f"Неизвестная валюта: {currency}")

    return round(amount * rate, 2)