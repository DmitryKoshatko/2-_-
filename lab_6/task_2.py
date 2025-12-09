def task2():
    # Ввод маски
    mask = input("Введите маску (с одним * и одним ?): ")

    # Ввод диапазона
    a = int(input("Введите начало диапазона: "))
    b = int(input("Введите конец диапазона: "))

    # Функция проверки соответствия числа маске
    def matches_mask(num, mask):
        num_str = str(num)

        # Разделяем маску на части по символу *
        if '*' in mask:
            parts = mask.split('*')
            before_star = parts[0]
            after_star = parts[1]

            # Проверяем, что в after_star есть ?
            if '?' in after_star:
                # Разделяем на части по ?
                question_parts = after_star.split('?')
                middle_part = question_parts[0]
                end_part = question_parts[1] if len(question_parts) > 1 else ""

                # Проверяем соответствие шаблону
                # Число должно начинаться с before_star
                if not num_str.startswith(before_star):
                    return False

                # Должна быть хотя бы одна цифра между * и ?
                remaining = num_str[len(before_star):]

                # Проверяем, что есть хотя бы одна цифра и заканчивается на end_part
                if len(remaining) < 1 + len(middle_part) + len(end_part):
                    return False

                # Проверяем среднюю часть
                if not remaining[len(remaining) - len(middle_part) - len(end_part) - 1:].startswith(middle_part):
                    return False

                # Проверяем конец
                if not remaining.endswith(end_part):
                    return False

                # Все проверки пройдены
                return True

        return False

    # Ищем числа в диапазоне, соответствующие маске
    matching_numbers = []
    for num in range(a, b + 1):
        if matches_mask(num, mask):
            matching_numbers.append(num)

    # Сортируем по убыванию
    matching_numbers.sort(reverse=True)

    # Выводим результат
    print("Числа, соответствующие маске:")
    for num in matching_numbers:
        print(num, end=" ")
    if not matching_numbers:
        print("Числа не найдены")


if __name__ == "__main__":
    task2()