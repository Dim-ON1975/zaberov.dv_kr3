import pytest

from src.utils.func import select_executed, list_sort, main, print_operations
from tests.conftest import TEST_NUMBER_TRANSACTIONS_DISPLAYED


def test_load_json(array_fixture: list):
    """
    Тестирование загрузки списка словарей из тестового файла json.
    Проверяем загружаются ли все значения из файла.
    Проверяем совпадает ли количество значений EXECUTED c ожидаемым.
    Проверяем совпадает ли количество значений CANCELED с ожидаемым.
    :return: Ошибки, если они имеются.
    """
    # Количество словарей всего
    assert len(array_fixture) == 8
    # Количество словарей EXECUTED
    count_executed = 0
    for value in array_fixture:
        if value['state'] == 'EXECUTED':
            count_executed += 1
    assert count_executed == 6
    # Количество словарей CANCELED
    count_canceled = 0
    for value in array_fixture:
        if value['state'] == 'CANCELED':
            count_canceled += 1
    assert count_canceled == 2


@pytest.mark.parametrize('date_str', [
    ['2018-03-23T10:45:06.972075',
     '2018-08-19T04:27:37.904916',
     '2018-01-26T15:40:13.413061',
     '2018-11-29T07:18:23.941293',
     '2019-04-04T23:20:05.206878',
     '2019-05-19T12:51:49.023880']
])
def test_select_executed(array_fixture: list, date_str: list):
    """
    Тестирование формирования списка словарей выполненных операций (EXECUTED)
    :return: Ошибки, если они имеются.
    """
    assert len(select_executed(array_fixture)) == 6
    test_list = select_executed(array_fixture)
    for value in test_list:
        assert value.get('date') in date_str


def test_list_sort(array_fixture: list):
    """
    Тестирование сортировки списка словарей по дате и времени
    :param array_fixture: несортированный список, lst
    :return: Ошибки, если они имеются.
    """
    assert list_sort(select_executed(array_fixture)) == [
        {
            "id": 179194306,
            "state": "EXECUTED",
            "date": "2019-05-19T12:51:49.023880",
            "operationAmount": {
                "amount": "6381.58",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "МИР 5211277418228469",
            "to": "Счет 58518872592028002662"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 518707726,
            "state": "EXECUTED",
            "date": "2018-11-29T07:18:23.941293",
            "operationAmount": {
                "amount": "3348.98",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 3152479541115065",
            "to": "Visa Gold 9447344650495960"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {
            "id": 147815167,
            "state": "EXECUTED",
            "date": "2018-01-26T15:40:13.413061",
            "operationAmount": {
                "amount": "50870.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 4598300720424501",
            "to": "Счет 43597928997568165086"
        }
    ]


def test_print_operations():
    """
    Тест функции, которая не возвращает значений посредством return
    :return: Ошибки, если они имеются.
    """
    list_dict = [
        {
            "id": 179194306,
            "state": "EXECUTED",
            "date": "2019-05-19T12:51:49.023880",
            "operationAmount": {
                "amount": "6381.58",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "МИР 5211277418228469",
            "to": "Счет 58518872592028002662"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 518707726,
            "state": "EXECUTED",
            "date": "2018-11-29T07:18:23.941293",
            "operationAmount": {
                "amount": "3348.98",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 3152479541115065",
            "to": "Visa Gold 9447344650495960"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {
            "id": 147815167,
            "state": "EXECUTED",
            "date": "2018-01-26T15:40:13.413061",
            "operationAmount": {
                "amount": "50870.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 4598300720424501",
            "to": "Счет 43597928997568165086"
        }
    ]
    number_operations = TEST_NUMBER_TRANSACTIONS_DISPLAYED
    assert print_operations(list_dict, number_operations) is None


def test_main():
    """
    Тест функции, которая не возвращает значений посредством return
    :return: Ошибки, если они имеются.
    """
    assert main() is None
