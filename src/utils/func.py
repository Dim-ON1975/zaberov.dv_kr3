# Функции
import json
from datetime import datetime

from src.utils.constants import PATH_OPERATIONS


def load_json(path_json: str) -> list:
    """
    Чтение данных из файла json и возвращение структуры,
    содержащейся в файле
    :param path_json: путь к файлу, str
    :return: структура файла (список, словарь, список словарей...)
    """
    # открываем файл на чтение
    with open(path_json, 'r', encoding='utf-8') as file:
        # считываем список словарей из файла
        content = json.load(file)
    return content


def select_executed(operations: list) -> list:
    """
    Возвращает список словарей с выполненными операциями.
    :param operations: список словарей всех операций, list
    :return: список словарей выполненных операций, list
    """
    list_executed = []
    for value in operations:
        if value.get('state') == 'EXECUTED':
            # Заменяем в строке с датой и временем T на пробел
            date_time = value.get('date').replace('T', ' ')
            value['date'] = date_time
            list_executed.append(value)
    return list_executed


def list_sort(list_operations: list) -> list:
    """
    Возвращает список словарей, сортированный по дате и времени
    в обратном порядке.
    :param list_operations: несортированный список словарей, list
    :return: сортированный список словарей, list
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
