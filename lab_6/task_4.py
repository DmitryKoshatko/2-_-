def task4():
    # Исходный список
    items = ['a', 'b', 'a', 'c', 'b', 'd', 'a', 'c']

    print("Исходный список:", items)

    # Создаем новый список для уникальных элементов
    unique_items = []

    for item in items:
        # Если элемента еще нет в новом списке, добавляем его
        if item not in unique_items:
            unique_items.append(item)

    print("Список без повторений:", unique_items)

    # Альтернативный способ с сохранением порядка
    print("\nАльтернативный способ:")
    result = []
    for i in range(len(items)):
        # Проверяем, встречался ли элемент ранее
        found = False
        for j in range(i):
            if items[j] == items[i]:
                found = True
                break

        # Если не встречался, добавляем
        if not found:
            result.append(items[i])

    print("Результат:", result)


if __name__ == "__main__":
    task4()