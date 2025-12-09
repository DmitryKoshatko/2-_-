def task5():
    # Исходные данные
    grades = [5, 3, 4, 5, 2, 5, 3, 4, 4, 5, 2, 3]

    print("Оценки студентов:", grades)
    print()

    # 1. Средний балл
    total = 0
    for grade in grades:
        total += grade

    average = total / len(grades)
    print(f"1. Средний балл: {average:.2f}")

    # 2. Сколько студентов получили "отлично" (оценка 5)
    excellent_count = 0
    for grade in grades:
        if grade == 5:
            excellent_count += 1

    print(f"2. Студентов с оценкой 'отлично' (5): {excellent_count}")

    # 3. Минимальная и максимальная оценка
    min_grade = grades[0]
    max_grade = grades[0]

    for grade in grades:
        if grade < min_grade:
            min_grade = grade
        if grade > max_grade:
            max_grade = grade

    print(f"3. Минимальная оценка: {min_grade}")
    print(f"   Максимальная оценка: {max_grade}")

    # 4. Сортировка по возрастанию (без sort())
    print("\n4. Сортировка оценок:")

    # Сортировка по возрастанию (метод пузырька)
    asc_grades = grades.copy()  # Создаем копию списка

    for i in range(len(asc_grades)):
        for j in range(len(asc_grades) - 1 - i):
            if asc_grades[j] > asc_grades[j + 1]:
                # Меняем элементы местами
                asc_grades[j], asc_grades[j + 1] = asc_grades[j + 1], asc_grades[j]

    print(f"   По возрастанию: {asc_grades}")

    # Сортировка по убыванию
    desc_grades = grades.copy()  # Создаем копию списка

    for i in range(len(desc_grades)):
        for j in range(len(desc_grades) - 1 - i):
            if desc_grades[j] < desc_grades[j + 1]:
                # Меняем элементы местами
                desc_grades[j], desc_grades[j + 1] = desc_grades[j + 1], desc_grades[j]

    print(f"   По убыванию: {desc_grades}")


if __name__ == "__main__":
    task5()