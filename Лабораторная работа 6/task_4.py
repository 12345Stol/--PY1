import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line="\n") -> list[dict]:
    with open(filename) as file:
        headers = file.readline().strip(new_line).split(delimiter)
        return [dict(zip(headers, str_.strip(new_line).split(delimiter))) for str_ in file]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
