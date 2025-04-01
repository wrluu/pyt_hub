import json
import os


def read_json(file_path):
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, IOError):
        return []