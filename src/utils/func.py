# Функции

import json
import os

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
    Выводит список словарей с выполненными операциями
    :param operations: список словарей всех операций, list
    :return: список словарей выполненных операций, list
    """
    list_executed = []
    for value in operations:
        if value.get('state') == 'EXECUTED':
            list_executed.append(value)
    return list_executed


def main() -> None:
    """
    Основной код программы
    """
    # содержимое файла
    content = load_json(PATH_OPERATIONS)
    # список словарей выполненных операций
    exec_list = select_executed(content)
