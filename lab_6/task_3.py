def task3():
    # Исходные данные
    weather = [
        ('Пн', -2, 3, -1),
        ('Вт', 0, 5, 1),
        ('Ср', -1, 4, -2),
        ('Чт', 2, 7, 3),
        ('Пт', 1, 6, 2)
    ]

    print("Данные о погоде:")
    for day in weather:
        print(f"{day[0]}: утро={day[1]}°, день={day[2]}°, ночь={day[3]}°")
    print()

    # 1. День с самой высокой дневной температурой
    max_day_temp = -100
    max_day_name = ""

    for day in weather:
        if day[2] > max_day_temp:  # day[2] - температура днем
            max_day_temp = day[2]
            max_day_name = day[0]

    print(f"1. Самый теплый день: {max_day_name} ({max_day_temp}°)")

    # 2. Средняя температура за неделю
    total_temps = 0
    total_measurements = 0

    for day in weather:
        total_temps += day[1] + day[2] + day[3]  # Суммируем все три измерения
        total_measurements += 3

    avg_temp = total_temps / total_measurements
    print(f"2. Средняя температура за неделю: {avg_temp:.1f}°")

    # 3. Дни, когда средняя температура за день была выше нуля
    days_above_zero = 0

    for day in weather:
        day_avg = (day[1] + day[2] + day[3]) / 3
        if day_avg > 0:
            days_above_zero += 1

    print(f"3. Дней с средней температурой выше нуля: {days_above_zero}")


if __name__ == "__main__":
    task3()