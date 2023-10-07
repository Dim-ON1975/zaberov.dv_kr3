import os
import pytest

from src.utils.func import load_json

# Путь к тестовому файлу данных
PATH_TEST_OPERATIONS = os.path.join('..', 'tests', 'data', 'test_operations.json')

# Количество выводимых операций
TEST_NUMBER_TRANSACTIONS_DISPLAYED = 5

# Массив с данными
ARRAY = load_json(PATH_TEST_OPERATIONS)


@pytest.fixture
def array_fixture():
    return ARRAY.copy()
