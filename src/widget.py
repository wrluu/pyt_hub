from module_of_mask import get_mask_card_number, get_mask_account

def mask_account_card(card_info):
    """
    Принимает на вход строку формата "Visa Platinum 7000792289606361", "Maestro 7000792289606361" и "Счет 73654108430135874305"
    """
    if "Счет" in card_info:
        return get_mask_account(card_info)
    else:
        return get_mask_card_number(card_info)

def get_date(date_str):
    """
    Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    try:
        date_part = date_str.split('T')[0]
        year, month, day = date_part.split('-')
        return f"{day}.{month}.{year}"
    except ValueError:
        raise ValueError("Неверный формат даты")

if __name__ == "__main__":
     card_info = input()
     account_info = input()
     date_str = input()

     print(mask_account_card(card_info))
     print(mask_account_card(account_info))
     print(get_date(date_str))