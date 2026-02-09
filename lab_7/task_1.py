from collections import defaultdict, Counter


def task1():
    attendance = {
        "2025-03-12": ["Иван", "Мария", "Петр", "Анна"],
        "2025-03-14": ["Иван", "Анна", "Сергей"],
        "2025-03-17": ["Мария", "Петр", "Сергей"],
        "2025-03-19": ["Иван", "Мария", "Петр", "Анна", "Сергей"],
        "2025-03-21": ["Иван", "Петр"]
    }

    # Все студенты
    all_students = {student for students in attendance.values() for student in students}

    # Подсчет посещений
    total_classes = len(attendance)
    attendance_count = defaultdict(int)

    for students in attendance.values():
        for student in students:
            attendance_count[student] += 1

    # Находим студента с максимальными пропусками
    max_absences_student = min(attendance_count, key=attendance_count.get)
    max_absences = total_classes - attendance_count[max_absences_student]

    print(f"1. Больше всех пропустил: {max_absences_student} ({max_absences} занятий)\n")

    # Процент посещаемости
    print("2. Процент посещаемости:")
    for student in sorted(all_students):
        percentage = (attendance_count[student] / total_classes) * 100
        print(f"   {student}: {percentage:.1f}%")


if __name__ == "__main__":
    task1()