import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line="\n") -> list[dict]:
    with open(filename) as file:
        list_ = []
        for i, row in enumerate(file):
            value = row.strip(new_line).split(delimiter)
            if i == 0:  # Если на первой строке
                column = value  # То записываем как заголовки
                continue
            list_.append({})  # Добавим новый словарь в список
            for index, head in enumerate(column):
                list_[-1][column[index]] = value[index]  # В последний созданный словарь в списке добавляем поочередно значения

    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
