def task5():
    def convert_number(num_str, from_base, to_base):
        """Конвертирует число из одной системы счисления в другую"""
        # Преобразуем в десятичную систему
        decimal_num = int(num_str, from_base)

        # Преобразуем в целевую систему счисления
        if to_base == 10:
            return str(decimal_num)

        # Для систем счисления от 2 до 9
        digits = []
        n = decimal_num

        if n == 0:
            return "0"

        while n > 0:
            digits.append(str(n % to_base))
            n //= to_base

        return ''.join(reversed(digits))

    # Ввод количества заданий
    n = int(input("Введите количество чисел: "))

    result_list = []

    for i in range(n):
        # Ввод строки с числом и его основанием
        line = input(f"Введите число {i + 1} и его основание: ").strip()
        num_str, from_base_str = line.split()
        from_base = int(from_base_str)

        # Ввод оснований для перевода
        to_bases = list(map(int, input(f"Введите основания для перевода числа {i + 1}: ").split()))

        # Создаем словарь для текущего числа
        conversion_dict = {}

        # Добавляем исходное представление
        conversion_dict[str(from_base)] = num_str

        # Конвертируем во все требуемые основания
        for to_base in to_bases:
            result = convert_number(num_str, from_base, to_base)
            conversion_dict[str(to_base)] = result

        # Добавляем словарь в список результатов
        result_list.append(conversion_dict)

    # Вывод результата
    print("\nРезультат:")
    print(result_list)


if __name__ == "__main__":
    task5()