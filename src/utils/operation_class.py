from src.utils.constants import NUM_CARD


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
    def date_formatted(self) -> str:
        """
        Возвращает дату типа 2023-10-06 в виде 06.10.2023
        :return: Строка, str
        """
        # Получение списка строк, содержащих элементы даты,
        # расположив элементы списка в обратном порядке [::-1]
        date_split = self.dict_operations.get('date')[0:10].split('-')[::-1]

        # Создание строки из списка
        date_formatted: str = '.'.join(date_split)

        return date_formatted

    @property
    def description_print(self) -> str:
        """
        Возвращает строку, содержащую информацию о назначении платежа
        :return: Строка, str
        """
        description_str: str = self.dict_operations['description']
        return description_str

    def from_to(self) -> str:
        """
        Возвращает строку, содержащую информацию о счетах перевода или открытых счетах
        :return: Строка, str
        """
        if 'from' in self.dict_operations:
            # Маскируем значение словаря по ключу 'from'
            str_from = self.dict_operations['from']  # строковое значение по ключу 'from'
            len_num_from = len(str_from.split(' ')[-1])  # длина последовательности из цифр
            mask_from = self.mask_bank_card(str_from) if len_num_from == NUM_CARD else self.mask_bank_account(
                str_from)

            # Маскируем значение словаря по ключу 'to'
            str_to = self.dict_operations['to']  # строковое значение по ключу 'to'
            len_num_to = len(str_to.split(' ')[-1])  # длина последовательности из цифр
            mask_to = self.mask_bank_card(str_to) if len_num_to == NUM_CARD else self.mask_bank_account(str_to)

            # "Собираем" строку для вывода
            mask: str = mask_from + ' -> ' + mask_to
        else:
            # Маскируем значение словаря по ключу 'to'
            mask_to = self.mask_bank_account(self.dict_operations['to'])

            # "Собираем" строку для вывода
            mask: str = mask_to

        return mask

    @staticmethod
    def mask_bank_card(number_str: str) -> str:
        """
        Маскирование банковской карты, например, МИР 5211 27** **** 8469
        :param number_str: Строка, содержащая название и номер банковской карты, str
        :return: Строка, содержащая название и замаскированный номер банковской карты, str
        """
        # Помещаем строки, разделённые пробелом в список
        card = number_str.split(' ')

        # Берём последний элемент списка - номер карты - строка 16 цифр: card[-1]
        # Создаём маску номера, разделив пробелами по 4 группы символов
        card[-1] = card[-1][:4] + ' ' + card[-1][4:6] + '** **** ' + card[-1][-4:]

        return ' '.join(card)

    @staticmethod
    def mask_bank_account(number_str: str) -> str:
        """
        Маскирование банковского счёта, например, Счет **2662
        :param number_str: Строка, содержащая название и номер банковского счёта, str
        :return: Строка, содержащая название и замаскированный номер банковского счёта, str
        """
        # Помещаем строки, разделённые пробелом в список
        account = number_str.split(' ')

        # Берём последний элемент списка - номер счёта - строка 20 цифр: account[-1]
        # Создаём маску номера
        account[-1] = '**' + account[-1][-4:]

        return ' '.join(account)

    @property
    def amount_transfer(self) -> str:
        """
        Возвращает строку, содержащую информацию о сумме перевода
        :return: Строка, str
        """
        amount = self.dict_operations['operationAmount']['amount']
        currency_name = self.dict_operations['operationAmount']['currency']['name']
        return amount + ' ' + currency_name

    def __repr__(self):
        return f'Operation ({self.dict_operations})'
