import json
import os
import logging

logs_directory = 'logs'
os.makedirs(logs_directory, exist_ok=True)

utils_logger = logging.getLogger('utils')
utils_logger.setLevel(logging.DEBUG)

utils_file_handler = logging.FileHandler(os.path.join(logs_directory, 'utils.log'), mode='w')

utils_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
utils_file_handler.setFormatter(utils_file_formatter)

utils_logger.addHandler(utils_file_handler)

def read_json(file_path):
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                utils_logger.debug(f'Successfully read JSON file: {file_path}')
                return data
            else:
                utils_logger.error(f'JSON file does not contain a list: {file_path}')
                return []
    except (json.JSONDecodeError, IOError) as e:
        utils_logger.error(f'Error reading JSON file {file_path}: {e}')
        return []
