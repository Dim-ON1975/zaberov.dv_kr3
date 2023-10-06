import pytest

from src.utils.func import select_executed
from src.utils.operation_class import Operation
from tests.conftest import ARRAY


@pytest.mark.parametrize('test_dict, expected', [
    (select_executed(ARRAY)[0], '19.05.2019'),
    (select_executed(ARRAY)[1], '04.04.2019')
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
