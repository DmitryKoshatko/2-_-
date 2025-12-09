def task4():
    print("Ввод рецептов (окончание - точка):")

    # Чтение рецептов
    recipes = {}
    while True:
        line = input().strip()
        if line.endswith('.'):
            # Убираем точку
            line = line[:-1].strip()
            if line:
                # Разделяем название и ингредиенты
                if ': ' in line:
                    name, ingredients_str = line.split(': ', 1)
                    # Разделяем ингредиенты
                    ingredients = [ing.strip() for ing in ingredients_str.split(', ')]
                    recipes[name] = ingredients
            break
        elif line.endswith(';'):
            # Убираем точку с запятой
            line = line[:-1].strip()
            if line:
                if ': ' in line:
                    name, ingredients_str = line.split(': ', 1)
                    ingredients = [ing.strip() for ing in ingredients_str.split(', ')]
                    recipes[name] = ingredients

    print("\nВвод продуктов в холодильнике (окончание - точка):")

    # Чтение продуктов в холодильнике
    fridge = {}
    while True:
        line = input().strip()
        if line.endswith('.'):
            line = line[:-1].strip()
            if line:
                if ': ' in line:
                    item, count_str = line.split(': ', 1)
                    fridge[item.strip()] = int(count_str)
            break
        elif line.endswith(';'):
            line = line[:-1].strip()
            if line:
                if ': ' in line:
                    item, count_str = line.split(': ', 1)
                    fridge[item.strip()] = int(count_str)

    print("\nВвод рецептов для приготовления (пустая строка - окончание):")

    # Чтение рецептов для приготовления
    dishes_to_cook = []
    while True:
        dish = input().strip()
        if not dish:
            break
        dishes_to_cook.append(dish)

    print("\n" + "=" * 50)
    print("Результат:")
    print("=" * 50)

    # Приготовление блюд
    for dish in dishes_to_cook:
        if dish not in recipes:
            print(f"Рецепт '{dish}' не найден")
            continue

        # Проверяем, достаточно ли ингредиентов
        can_cook = True
        needed_ingredients = recipes[dish]

        # Создаем временную копию для проверки
        temp_fridge = fridge.copy()

        for ingredient in needed_ingredients:
            if ingredient not in temp_fridge or temp_fridge[ingredient] == 0:
                can_cook = False
                break
            temp_fridge[ingredient] -= 1

        if can_cook:
            # Приготовление возможно - обновляем холодильник
            for ingredient in needed_ingredients:
                fridge[ingredient] -= 1
            print(f"Готовим {dish}.")
        else:
            print(f"Приготовить {dish} не получится.")

    # Выводим оставшиеся продукты
    print("\n" + "=" * 50)
    print("Остатки в холодильнике:")
    for item, count in fridge.items():
        if count > 0:
            print(f"  {item}: {count}")


if __name__ == "__main__":
    task4()