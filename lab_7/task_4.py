def read_until_end_marker(end_marker='.'):
    """Читает строки до маркера окончания"""
    lines = []
    while True:
        line = input().strip()
        if not line:
            continue
        if line.endswith(end_marker):
            lines.append(line.rstrip(end_marker).strip())
            break
        lines.append(line.rstrip(';').strip())
    return lines


def task4():
    print("Ввод рецептов (окончание - точка):")
    recipes = {}
    for line in read_until_end_marker():
        if ': ' in line:
            name, ingredients = line.split(': ', 1)
            recipes[name] = [i.strip() for i in ingredients.split(', ')]

    print("\nВвод продуктов в холодильнике:")
    fridge = {}
    for line in read_until_end_marker():
        if ': ' in line:
            item, count = line.split(': ', 1)
            fridge[item.strip()] = int(count)

    print("\nВвод блюд для приготовления (пустая строка - окончание):")
    dishes = []
    while True:
        dish = input().strip()
        if not dish:
            break
        dishes.append(dish)

    print("\n" + "=" * 50 + "\nРезультат:\n" + "=" * 50)

    for dish in dishes:
        if dish not in recipes:
            print(f"Рецепт '{dish}' не найден")
            continue

        # Проверка возможности приготовления
        needed = recipes[dish]
        can_cook = all(fridge.get(ing, 0) > 0 for ing in needed)

        if can_cook:
            for ing in needed:
                fridge[ing] -= 1
            print(f"Готовим {dish}.")
        else:
            print(f"Приготовить {dish} не получится.")

    # Остатки
    print("\n" + "=" * 50 + "\nОстатки в холодильнике:")
    for item, count in sorted(fridge.items()):
        if count > 0:
            print(f"  {item}: {count}")


if __name__ == "__main__":
    task4()