def task4():
    year = int(input("Введите год: "))

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Год високосный")
    else:
        print("Год не високосный")


if __name__ == "__main__":
    task4()