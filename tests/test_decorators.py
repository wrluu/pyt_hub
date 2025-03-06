import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from decorators import log

@log()
def add(x, y):
    """
    Функция сложения двух чисел
    """
    return x + y

@log(filename="test_log.txt")
def divide(x, y):
    """
    Функция деления двух чисел
    """
    return x / y

def test_log_to_console(capsys):
    """
    Тест для проверки логирования в консоль
    """
    assert add(1, 2) == 3
    captured = capsys.readouterr()
    assert "add ok" in captured.out

def test_log_to_file():
    """
    Тест для проверки логирования в файл
    """
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    with open("test_log.txt", "r") as f:
        logs = f.read()
        assert "divide error: ZeroDivisionError" in logs

def test_log_exception_to_console(capsys):
    """
    Тест для проверки логирования исключений в консоль
    """
    @log()
    def fail():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        fail()

    captured = capsys.readouterr()
    assert "fail error: ValueError" in captured.err
