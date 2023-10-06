from src.utils.func import select_executed, main


def test_load_json(array_fixture):
    """
    Тестирование загрузки списка словарей из тестового файла json.
    Проверяем загружаются ли все значения из файла.
    Проверяем совпадает ли количество значений EXECUTED c ожидаемым.
    Проверяем совпадает ли количество значений CANCELED с ожидаемым.
    :return: ошибки, если они имеются.
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


def test_select_executed(array_fixture):
    """
    Тестирование формирования списка словарей выполненных операций (EXECUTED).
    :return: ошибки, если они имеются.
    """
    assert len(select_executed(array_fixture)) == 6


def test_main():
    """
    Тест функции, которая не возвращает значений посредством return
    :return: ошибки, если они имеются.
    """
    assert main() is None
