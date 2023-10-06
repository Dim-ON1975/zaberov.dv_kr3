class Operation:
    """
    Класс выполненной операции
    """

    def __init__(self, dict_operations: dict) -> None:
        """
        Инициализация класса
        :param dict_operations: Выполненная операция, dict
        """
        self.dict_operations = dict_operations

    @property
    def date_formatted(self):
        """
        Возвращает дату типа 2023-10-06 в виде 06.10.2023
        :return: Строка, str
        """
        # Получение списка строк, содержащих элементы даты,
        # расположив элементы списка в обратном порядке [::-1]
        date_split = self.dict_operations.get('date')[0:10].split('-')[::-1]

        # Создание строки из списка
        date_formatted = '.'.join(date_split)

        return date_formatted
