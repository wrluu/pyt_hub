import os
import requests

API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")
BASE_URL = f"http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&base=USD"

def convert_currency(transaction):
    """
    Функция для конвертации валюты в рубли.
    """
    amount = float(transaction['operationAmount']['amount'])
    currency = transaction['operationAmount']['currency']['code']

    if currency == 'RUB':
        return amount

    response = requests.get(BASE_URL)
    rates = response.json().get('rates', {})

    if currency == 'USD':
        rate = rates.get('RUB', 1.0)
    elif currency == 'EUR':
        rub_rate = rates.get('RUB', 1.0)
        eur_rate = rates.get('EUR', 1.0)
        rate = rub_rate / eur_rate
    else:
        raise ValueError(f"Неизвестная валюта: {currency}")

    return round(amount * rate, 2)
