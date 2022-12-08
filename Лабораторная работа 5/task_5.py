from random import sample
import string


def get_random_password() -> str:
    n = 8  # Допустимое кол-во символов в пароле
    list_symbols = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)  # Обозначим список допустимых символов
    random_password = "".join(sample(list_symbols, n))  # Генерируем случайную выборку символов для пароля
    return random_password


print(get_random_password())

