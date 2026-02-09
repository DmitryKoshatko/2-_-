def task5():
    n = int(input())
    results = []

    for _ in range(n):
        num_str, base_from = input().split()
        base_from = int(base_from)
        bases_to = list(map(int, input().split()))

        # Конвертируем в десятичную один раз
        decimal = int(num_str, base_from)

        # Создаем словарь преобразований
        conversions = {str(base_from): num_str}
        for base in bases_to:
            if base == 10:
                conversions[str(base)] = str(decimal)
            else:
                # Преобразование в любую систему
                if decimal == 0:
                    conversions[str(base)] = "0"
                else:
                    digits = []
                    n = decimal
                    while n > 0:
                        digits.append(str(n % base))
                        n //= base
                    conversions[str(base)] = ''.join(reversed(digits))

        results.append(conversions)

    print(results)


if __name__ == "__main__":
    task5()