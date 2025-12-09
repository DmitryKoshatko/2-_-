def task2():
    n = int(input("Введите число: "))

    divisors_sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisors_sum += i

    print(f"Сумма делителей числа {n}: {divisors_sum}")


if __name__ == "__main__":
    task2()