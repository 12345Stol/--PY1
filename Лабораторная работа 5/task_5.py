from random import sample
from string import ascii_uppercase, ascii_lowercase, digits


def get_random_password(n=8) -> str:
    symbol = ascii_uppercase + ascii_lowercase + digits  # Обозначим допустимые символы
    random_password = "".join(sample(symbol, n))  # Генерируем случайную выборку символов для пароля
    return random_password


print(get_random_password())
