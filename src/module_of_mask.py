import logging
import os

logs_directory = 'logs'
os.makedirs(logs_directory, exist_ok=True)

masks_logger = logging.getLogger('masks')
masks_logger.setLevel(logging.DEBUG)

masks_file_handler = logging.FileHandler(os.path.join(logs_directory, 'masks.log'), mode='w')

masks_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
masks_file_handler.setFormatter(masks_file_formatter)

masks_logger.addHandler(masks_file_handler)

def get_mask_card_number(card_info):
    """
    Принимает на вход строку с типом и номером карты и возвращает маску номера по правилу XXXX XX** **** XXXX
    """
    try:
        parts = card_info.split()
        card_number = parts[-1]
        if len(card_number) != 16:
            raise ValueError("Номер карты должен содержать 16 цифр.")
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        masks_logger.debug(f'Successfully masked card number: {masked_number}')
        return ' '.join(parts[:-1]) + ' ' + masked_number
    except Exception as e:
        masks_logger.error(f'Error masking card number: {e}')
        raise

def get_mask_account(account_info):
    """
    Принимает на вход строку с типом и номером счета и возвращает маску номера по правилу **XXXX
    """
    try:
        parts = account_info.split()
        account_number = parts[-1]
        if len(account_number) < 6:
            raise ValueError("Номер счета должен содержать не менее 6 цифр.")
        if len(account_number) == 6:
            masked_number = '**' + account_number[-3:]
        else:
            masked_number = '**' + account_number[-4:]
        masks_logger.debug(f'Successfully masked account number: {masked_number}')
        return ' '.join(parts[:-1]) + ' ' + masked_number
    except Exception as e:
        masks_logger.error(f'Error masking account number: {e}')
        raise
