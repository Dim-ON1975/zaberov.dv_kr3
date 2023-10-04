import os
import pytest

from src.utils.func import load_json

# Путь к тестовому файлу данных
PATH_TEST_OPERATIONS = os.path.join('..', 'tests', 'data', 'test_operations.json')

ARRAY = load_json(PATH_TEST_OPERATIONS)


@pytest.fixture
def array_fixture():
    return ARRAY.copy()
