def task2():
    print("Введите строки (пустая строка для завершения):")

    def transform_string(s):
        """Функция преобразования строки по правилам автомата"""
        while True:
            original = s

            # Заменяем по порядку согласно условию
            if '111' in s:
                s = s.replace('111', '0', 1)  # Замена первых слева трех единиц
            elif '000' in s:
                s = s.replace('000', '1', 1)  # Замена первых слева трех нулей
            elif '001' in s:
                s = s.replace('001', '1', 1)  # Замена 001 на 1
            elif '100' in s:
                s = s.replace('100', '1', 1)  # Замена 100 на 1
            elif '00' in s:
                s = s.replace('00', '0', 1)  # Замена 00 на 0
            else:
                break  # Если ни одно условие не выполнилось

            # Если строка не изменилась, выходим
            if s == original:
                break

        return s

    # Считываем строки до пустой строки
    input_strings = []
    while True:
        s = input().strip()
        if s == "":
            break
        # Проверяем, что строка состоит только из 0 и 1
        if all(char in '01' for char in s):
            input_strings.append(s)
        else:
            print("Строка должна содержать только 0 и 1!")

    # Преобразуем все строки
    transformed_strings = [transform_string(s) for s in input_strings]

    # Используем множество для получения уникальных строк
    unique_strings = set(transformed_strings)

    # Выводим результат
    print(f"\nКоличество различных строк: {len(unique_strings)}")
    print("Полученные строки:")
    for s in sorted(unique_strings):
        print(s)


if __name__ == "__main__":
    task2()