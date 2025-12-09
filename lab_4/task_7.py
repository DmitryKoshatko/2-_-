def task7():
    n = int(input("Введите число для таблицы умножения: "))

    for i in range(1, 11):
        for j in range(1, 11):
            if i == n or j == n:
                print(f"{i} x {j} = {i * j}")


if __name__ == "__main__":
    task7()