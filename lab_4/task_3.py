def task3():
    n = int(input("Введите начальный день (n): "))
    m = int(input("Введите шаг (m): "))

    dates = []
    for day in range(n, 32, m):
        dates.append(str(day))

    print(" ".join(dates))


if __name__ == "__main__":
    task3()