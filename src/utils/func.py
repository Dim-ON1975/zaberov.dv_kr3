# Функции
import json
from datetime import datetime

from src.utils.constants import PATH_OPERATIONS
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
    Возвращает список словарей с выполненными операциями.
    :param operations: Список словарей всех операций, list
    :return: Список словарей выполненных операций, list
    """
    list_executed = []
    for value in operations:
        if value.get('state') == 'EXECUTED':
            # Заменяем в строке с датой и временем T на пробел
            date_time = value.get('date').replace('T', ' ')
            value['date'] = date_time
            list_executed.append(value)
    # Сортируем список
    list_executed = list_sort(list_executed)
    return list_executed


def list_sort(list_operations: list) -> list:
    """
    Возвращает список словарей, сортированный по дате и времени
    в обратном порядке.
    :param list_operations: Несортированный список словарей, list
    :return: Сортированный список словарей, list
    """
    # Сортируем словари в списке по дате и времени в обратном порядке
    list_operations = sorted(list_operations,
                             key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S.%f'),
                             reverse=True)
    return list_operations


def main() -> None:
    """
    Основной код программы
    """
    # содержимое файла
    content = load_json(PATH_OPERATIONS)
    # список словарей выполненных операций
    exec_list = select_executed(content)

    # Извлекаем из словарей необходимую информацию, выводя ее на экран
    for dict_operation in exec_list[0:5]:
        # создаём экземпляр класса Operation
        operation = Operation(dict_operation)

        # Вывод данных на экран
        print(
            f'{operation.date_formatted}'
        )
