import random


def get_unique_list_numbers() -> list[int]:
    list_number = list(range(-10, 11))  # Создадим список значений от -10 до 10 включительно
    unique_number = random.sample(list_number, 15)  # Отберем 15 случайных уникальных значений
    return unique_number


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))


