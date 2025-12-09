def task2():
    a = input("Строка 1: ").strip().lower()
    b = input("Строка 2: ").strip().lower()
    c = input("Строка 3: ").strip().lower()

    # Собираем введённые значения в список и сортируем для сравнения
    inputs = sorted([a, b, c])

    # Ожидаемые наборы (отсортированные)
    correct_set1 = sorted(["раз", "два", "три"])
    correct_set2 = sorted(["1", "2", "3"])

    if inputs == correct_set1 or inputs == correct_set2:
        print("ГОРИ")
    else:
        print("НЕ ГОРИ")


if __name__ == "__main__":
    task2()