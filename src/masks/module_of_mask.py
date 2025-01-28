def get_mask_card_number(card_number):
    """
    Принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX
    """
    card_str = str(card_number)
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")
    return f"XXXX XX** **** {card_str[-4:]}"

def get_mask_account(account_number):
    """
    Принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX
    """
    account_str = str(account_number)
    if len(account_str) < 6:
        raise ValueError("Номер счета должен содержать не менее 6 цифр.")
    return f"**{account_str[-4:]}"

def main():
    try:
        card_number = int(input())
        account_number = int(input())

        print(get_mask_card_number(card_number))
        print(get_mask_account(account_number))
    except ValueError:
        print("Ошибка: Введенное значение не является корректным числом.")

if __name__ == "__main__":
    main()
