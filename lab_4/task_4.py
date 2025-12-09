def task4():
    target_letter = input("Введите букву для поиска: ")

    # Защита от некорректного ввода количества букв
    while True:
        try:
            count = int(input("Введите количество букв: "))
            if count > 0:  # Проверяем, что количество положительное
                break
            else:
                print("Количество должно быть положительным числом!")
        except ValueError:
            print("Ошибка! Введите целое число.")

    max_repeats = 0
    current_repeats = 0

    print(f"\nВведите {count} букв:")
    for i in range(count):
        letter = input(f"Буква {i + 1}: ").strip()
        if letter == target_letter:
            current_repeats += 1
            if current_repeats > max_repeats:
                max_repeats = current_repeats
        else:
            current_repeats = 0

    print(f"\nНаибольшее количество повторений буквы '{target_letter}' подряд: {max_repeats}")


if __name__ == "__main__":
    task4()