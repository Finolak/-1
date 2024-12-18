# TODO Напишите функцию для поиска индекса товара
def find_first_index(items, item_to_find):
    # Проверяем, находится ли элемент в списке
    if item_to_find in items:
        # Возвращаем индекс первого вхождения
        return items.index(item_to_find)
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_first_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
