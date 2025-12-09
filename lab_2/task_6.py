def task6():
    number = int(input("Введите трёхзначное число: "))

    # Извлекаем цифры
    first = number // 100
    second = (number // 10) % 10
    third = number % 10

    sum_first_third = first + third

    if second == 3 and sum_first_third % 8 != 0:
        print("Подходит")
    else:
        print(sum_first_third, second)


if __name__ == "__main__":
    task6()