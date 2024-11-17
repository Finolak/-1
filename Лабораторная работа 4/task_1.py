# TODO решите задачу
import json

def task() -> float:
    with open("input.json", 'r') as file:
        data = json.load(file)

    # Вычисление суммы произведений
    total = sum(item["score"] * item["weight"] for item in data)

    # Возвращение результата, округленного до 3 знаков
    return round(total, 3)


print(task())
