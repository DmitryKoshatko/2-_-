def task1():
    # Исходные данные: словарь с датами и списками студентов
    attendance = {
        "2025-03-12": ["Иван", "Мария", "Петр", "Анна"],
        "2025-03-14": ["Иван", "Анна", "Сергей"],
        "2025-03-17": ["Мария", "Петр", "Сергей"],
        "2025-03-19": ["Иван", "Мария", "Петр", "Анна", "Сергей"],
        "2025-03-21": ["Иван", "Петр"]
    }

    print("Расписание посещений:")
    for date, students in attendance.items():
        print(f"{date}: {', '.join(students)}")
    print()

    # 1. Собираем всех уникальных студентов
    all_students = set()
    for students in attendance.values():
        all_students.update(students)

    # 2. Считаем пропуски для каждого студента
    total_classes = len(attendance)
    attendance_stats = {}
    absences_stats = {}

    for student in all_students:
        attended = 0
        for students in attendance.values():
            if student in students:
                attended += 1

        attendance_stats[student] = (attended / total_classes) * 100
        absences_stats[student] = total_classes - attended

    # 3. Находим студента с наибольшим количеством пропусков
    max_absences_student = max(absences_stats, key=absences_stats.get)
    max_absences = absences_stats[max_absences_student]

    print(f"1. Больше всех пропустил: {max_absences_student} ({max_absences} занятий)")
    print()

    # 4. Процент посещаемости для каждого студента
    print("2. Процент посещаемости:")
    for student in sorted(attendance_stats.keys()):
        print(f"   {student}: {attendance_stats[student]:.1f}%")


if __name__ == "__main__":
    task1()