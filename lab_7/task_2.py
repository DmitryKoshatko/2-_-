def task2():
    # Исходный инвентарь
    inventory = {
        "Микроскоп": 5,
        "Пробирки": 20,
        "Колбы": 15,
        "Весы": 3,
        "Реактивы": 10
    }

    # Словарь для учета выданного оборудования
    issued_items = {}

    def issue_equipment(student, item, quantity=1, min_required=1):
        """
        Функция для выдачи оборудования

        Параметры:
        student - имя студента
        item - название оборудования
        quantity - количество для выдачи (по умолчанию 1)
        min_required - минимальное количество, которое должно остаться
        """

        # Проверяем наличие оборудования
        if item not in inventory:
            print(f"Оборудование '{item}' не найдено в инвентаре")
            return False

        # Проверяем, достаточно ли оборудования
        if inventory[item] - quantity < min_required:
            print(f"Недостаточно оборудования '{item}' для выдачи")
            print(f"Доступно: {inventory[item]}, требуется: {quantity}")
            return False

        # Уменьшаем количество в инвентаре
        inventory[item] -= quantity

        # Добавляем в учет выданного
        if student not in issued_items:
            issued_items[student] = []

        # Добавляем оборудование в список выданного студенту
        for _ in range(quantity):
            issued_items[student].append(item)

        print(f"Выдано студенту {student}: {quantity} шт. '{item}'")
        return True

    # Демонстрация работы
    print("Начальный инвентарь:")
    for item, count in inventory.items():
        print(f"  {item}: {count} шт.")
    print()

    # Примеры выдачи
    issue_equipment("Иван", "Микроскоп")
    issue_equipment("Мария", "Пробирки", 3)
    issue_equipment("Петр", "Весы")
    issue_equipment("Анна", "Колбы", 2)

    # Попытка выдать больше, чем есть
    print()
    issue_equipment("Сергей", "Весы", 3, min_required=1)

    print("\nТекущий инвентарь:")
    for item, count in inventory.items():
        print(f"  {item}: {count} шт.")

    print("\nВыданное оборудование:")
    for student, items in issued_items.items():
        print(f"  {student}: {', '.join(items)}")


if __name__ == "__main__":
    task2()