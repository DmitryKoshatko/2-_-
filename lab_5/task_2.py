def task2():
    # Функция для преобразования строки по правилам
    def transform(s):
        while True:
            if '111' in s:
                # Заменяем первые три единицы на ноль
                s = s.replace('111', '0', 1)
            elif '000' in s:
                # Заменяем первые три нуля на единицу
                s = s.replace('000', '1', 1)
            elif '001' in s:
                # Заменяем 001 на 1
                s = s.replace('001', '1', 1)
            elif '100' in s:
                # Заменяем 100 на 1
                s = s.replace('100', '1', 1)
            elif '00' in s:
                # Заменяем 00 на 0
                s = s.replace('00', '0', 1)
            else:
                # Если ничего не нашли - выходим
                break
        return s

    # Вводим строки
    print("Введите строки из 0 и 1 (пустая строка - завершить):")
    strings = []

    while True:
        s = input().strip()
        if s == "":
            break
        # Проверяем, что строка состоит только из 0 и 1
        if all(c in '01' for c in s):
            strings.append(s)

    # Преобразуем все строки
    results = []
    for s in strings:
        results.append(transform(s))

    # Находим уникальные результаты
    unique_results = set(results)

    # Выводим ответ
    print(f"\nКоличество различных строк: {len(unique_results)}")
    print("Полученные строки:")
    for s in sorted(unique_results):
        print(s)


if __name__ == "__main__":
    task2()