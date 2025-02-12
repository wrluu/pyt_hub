import pytest
from module_of_widget import mask_account_card, get_date

@pytest.mark.parametrize("card_info, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
    ("Счет 73654108430135874305", "Счет **4305"),
])
def test_mask_account_card(card_info, expected):
    assert mask_account_card(card_info) == expected

@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-31T23:59:59.999999", "31.12.2023"),
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected

@pytest.mark.parametrize("date_str", [
    "2024-03-11 02:26:18.671407",  # Неверный формат
    "2024-03-11",  # Без времени
])
def test_get_date_invalid(date_str):
    with pytest.raises(ValueError, match="Неверный формат даты"):
        get_date(date_str)