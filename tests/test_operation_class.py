import pytest

from src.utils.func import select_executed
from src.utils.operation_class import Operation
from tests.conftest import ARRAY


@pytest.mark.parametrize('test_dict, expected', [
    (select_executed(ARRAY)[0], '19.05.2019'),
    (select_executed(ARRAY)[1], '04.04.2019'),
    (select_executed(ARRAY)[2], '29.11.2018'),
    (select_executed(ARRAY)[3], '19.08.2018'),
    (select_executed(ARRAY)[4], '23.03.2018'),
    (select_executed(ARRAY)[5], '26.01.2018'),
])
def test_date_formatted(test_dict: dict, expected: str):
    """
    Тестирование метода класса date_formatted(),
    форматирующая дату из 2023-10-06 в 06.10.2023
    :param test_dict: Словарь с данными операции, dict
    :param expected: Ожидаемый результат форматирования, str
    :return: Ошибки, если они имеются.
    """
    # Тестируем экземпляр класса Operation
    assert Operation(test_dict).date_formatted == expected


@pytest.mark.parametrize('test_dict, expected', [
    (select_executed(ARRAY)[0], 'Перевод организации'),
    (select_executed(ARRAY)[1], 'Перевод со счета на счет'),
    (select_executed(ARRAY)[2], 'Перевод с карты на карту'),
    (select_executed(ARRAY)[3], 'Перевод с карты на карту'),
    (select_executed(ARRAY)[4], 'Открытие вклада'),
    (select_executed(ARRAY)[5], 'Перевод с карты на счет'),
])
def test_description_print(test_dict: dict, expected: str):
    """
    Тестирование метода класса description_print,
    возвращающего строку о назначении платежа.
    :param test_dict: Словарь с данными операции, dict
    :param expected: Ожидаемый результат назначения платежа, str
    :return: Ошибки, если они имеются.
    """
    # Тестируем экземпляр класса Operation
    assert Operation(test_dict).description_print == expected


@pytest.mark.parametrize('test_dict, expected', [
    (select_executed(ARRAY)[0], 'МИР 5211 27** **** 8469 -> Счет **2662'),
    (select_executed(ARRAY)[1], 'Счет **8542 -> Счет **4188'),
    (select_executed(ARRAY)[2], 'MasterCard 3152 47** **** 5065 -> Visa Gold 9447 34** **** 5960'),
    (select_executed(ARRAY)[3], 'Visa Classic 6831 98** **** 7658 -> Visa Platinum 8990 92** **** 5229'),
    (select_executed(ARRAY)[4], 'Счет **2431'),
    (select_executed(ARRAY)[5], 'Maestro 4598 30** **** 4501 -> Счет **5086'),
])
def test_description_print(test_dict: dict, expected: str):
    """
    Тестирование метода класса description_print,
    возвращающего строку о назначении платежа.
    :param test_dict: Словарь с данными операции, dict
    :param expected: Ожидаемый результат назначения платежа, str
    :return: Ошибки, если они имеются.
    """
    # Тестируем экземпляр класса Operation
    assert Operation(test_dict).from_to() == expected
