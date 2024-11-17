# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open("input.csv", mode='r') as csv_file:
        # Чтение CSV файла
        reader = csv.DictReader(csv_file)
        # Преобразование в список словарей
        json_data = [row for row in reader]

    # TODO Сериализовать в файл с отступами равными 4
    with open("output.json", mode='w') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
