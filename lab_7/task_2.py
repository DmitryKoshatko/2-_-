from collections import defaultdict


class EquipmentManager:
    def __init__(self, inventory):
        self.inventory = inventory.copy()
        self.issued = defaultdict(list)

    def issue(self, student, item, quantity=1, min_required=0):
        """Выдать оборудование студенту"""
        if item not in self.inventory:
            print(f"Оборудование '{item}' не найдено")
            return False

        available = self.inventory[item]
        if available - quantity < min_required:
            print(f"Недостаточно '{item}'. Доступно: {available}, требуется: {quantity}")
            return False

        # Выдача
        self.inventory[item] -= quantity
        self.issued[student].extend([item] * quantity)
        print(f"Выдано студенту {student}: {quantity} шт. '{item}'")
        return True

    def print_status(self):
        print("\nТекущий инвентарь:")
        for item, count in self.inventory.items():
            print(f"  {item}: {count} шт.")

        print("\nВыданное оборудование:")
        for student, items in self.issued.items():
            print(f"  {student}: {', '.join(items)}")


def task2():
    inventory = {
        "Микроскоп": 5,
        "Пробирки": 20,
        "Колбы": 15,
        "Весы": 3,
        "Реактивы": 10
    }

    manager = EquipmentManager(inventory)

    print("Начальный инвентарь:")
    for item, count in inventory.items():
        print(f"  {item}: {count} шт.")

    # Выдача оборудования
    manager.issue("Иван", "Микроскоп")
    manager.issue("Мария", "Пробирки", 3)
    manager.issue("Петр", "Весы")
    manager.issue("Анна", "Колбы", 2)

    # Неудачная попытка
    print()
    manager.issue("Сергей", "Весы", 3, min_required=1)

    manager.print_status()


if __name__ == "__main__":
    task2()