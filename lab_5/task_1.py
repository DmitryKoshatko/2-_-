def task1():
    n = int(input("Введите число: "))

    # Разложение на простые множители
    original_n = n
    factors = []  # Все множители
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    # Уникальные множители (множество уберет дубликаты)
    unique_factors = sorted(set(factors))

    print("Все множители:", " ".join(map(str, factors)))
    print("Уникальные множители:", " ".join(map(str, unique_factors)))


if __name__ == "__main__":
    task1()