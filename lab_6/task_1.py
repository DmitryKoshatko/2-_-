def task1():
    # Ввод диапазона
    a = int(input("Введите начало диапазона: "))
    b = int(input("Введите конец диапазона: "))

    # Упорядочиваем границы диапазона
    start = min(a, b)
    end = max(a, b)

    # Функция преобразования числа по алгоритму
    def transform_number(num):
        # 1. Переводим в двоичную систему (убираем префикс '0b')
        binary = bin(num)[2:]

        # 2. Применяем правила
        if num % 2 == 0:  # Четное число
            binary = '11' + binary + '0'
        else:  # Нечетное число
            binary = binary + '10'

        # 3. Переводим обратно в десятичную систему
        result = int(binary, 2)
        return result

    # Применяем алгоритм ко всем числам в диапазоне
    results = []
    for num in range(start, end + 1):
        results.append(transform_number(num))

    # Находим минимальное и максимальное значение
    min_result = min(results)
    max_result = max(results)

    print(f"{min_result} {max_result}")


if __name__ == "__main__":
    task1()