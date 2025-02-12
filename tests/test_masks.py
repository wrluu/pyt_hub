import pytest
from module_of_mask import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_info, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
])
def test_get_mask_card_number(card_info, expected):
    assert get_mask_card_number(card_info) == expected

@pytest.mark.parametrize("card_info", [
    "Visa Platinum 700079228960636",
    "Maestro 123456789012345",
])
def test_get_mask_card_number_invalid(card_info):
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number(card_info)

@pytest.mark.parametrize("account_info, expected", [
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Счет 123456", "Счет **456"),
])
def test_get_mask_account(account_info, expected):
    assert get_mask_account(account_info) == expected

@pytest.mark.parametrize("account_info", [
    "Счет 12345",  # 5 цифр
    "Счет 123",  # 3 цифры
])
def test_get_mask_account_invalid(account_info):
    with pytest.raises(ValueError, match="Номер счета должен содержать не менее 6 цифр."):
        get_mask_account(account_info)