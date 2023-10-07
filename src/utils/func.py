# Функции
import json
from datetime import datetime

from src.utils.constants import PATH_OPERATIONS, NUMBER_TRANSACTIONS_DISPLAYED
from src.utils.operation_class import Operation


def load_json(path_json: str) -> list:
    """
    Чтение данных из файла json и возвращение структуры,
    содержащейся в файле.
    :param path_json: Путь к файлу, str
    :return: Структура файла (список, словарь, список словарей...)
    """
    # открываем файл на чтение
    with open(path_json, 'r', encoding='utf-8') as file:
        # считываем список словарей из файла
        content = json.load(file)
    return content


def select_executed(operations: list) -> list:
    """
    Возвращает, сортированный по датам и времени, список словарей с выполненными операциями.
    :param operations: Список словарей всех операций, list
    :return: Список словарей выполненных операций, list
    """
    list_executed = [value for value in operations if value.get('state') == 'EXECUTED']
    return list_sort(list_executed)


def list_sort(list_operations: list) -> list:
    """
    Возвращает список словарей, сортированный по дате и времени
    в обратном порядке.
    :param list_operations: Несортированный список словарей, list
    :return: Сортированный список словарей, list
    """
    # Сортируем словари в списке по дате и времени в обратном порядке
    list_operations = sorted(list_operations,
                             key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),
                             reverse=True)
    return list_operations


def print_operations(list_dict: list, number_operations: int) -> None:
    """
    Выводит на экран информацию о последних операциях
    :param list_dict: Список словарей, list
    :param number_operations: Количество отображаемых операций, int
    :return: Ничего не возвращает. Выводит на экран список последних операций
    """
    # Извлекаем из словарей необходимую информацию, выводя ее на экран
    for dict_operation in list_dict[0:number_operations]:
        # создаём экземпляр класса Operation
        operation = Operation(dict_operation)

        # Вывод данных на экран
        print(
            f'{operation.date_formatted} {operation.description_print}\n'
            f'{operation.from_to()}\n'
            f'{operation.amount_transfer}\n'
        )


def main() -> None:
    """
    Основной код программы
    """
    # содержимое файла
    content = load_json(PATH_OPERATIONS)
    # список словарей выполненных операций
    exec_list = select_executed(content)

    # вывод данных на экран
    print_operations(exec_list, NUMBER_TRANSACTIONS_DISPLAYED)
