from random import randint


def get_unique_list_numbers() -> list[int]:
    start = -10
    stop = 10
    symbols = 15
    list_number = []
    while len(list_number) < symbols:
        number = randint(start, stop)
        if number not in list_number:
            list_number.append(number)
    return list_number


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
