list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


max_index = 0  # Пусть максимальный элемент - это первый элемент списка
max_number = list_numbers[max_index]
for current_index, current_number in enumerate(list_numbers):  # Перебирем каждый элемент
    max_number = list_numbers[max_index]
    if current_number >= max_number:    # Если текущий элемент больше того, который встречали ранее
        max_index = current_index  # То перезапишем индекс элемента
        max_number = list_numbers[max_index]
list_numbers[19], list_numbers[max_index] = list_numbers[max_index], list_numbers[19]  # Меняем местами символы

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]

