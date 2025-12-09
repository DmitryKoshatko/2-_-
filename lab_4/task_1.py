def task1():
    # Функция для проверки, является ли число простым
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    total_sum = 0
    for number in range(1, 10001):
        if is_prime(number):
            total_sum += number

    print(f"Сумма всех простых чисел от 1 до 10000: {total_sum}")


if __name__ == "__main__":
    task1()