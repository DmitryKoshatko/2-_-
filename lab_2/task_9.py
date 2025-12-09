def task9():
    password = input("Введите пароль: ")
    special_symbols = set("!@#$%^&*")

    errors = []

    # 1. Длина
    if len(password) < 8:
        errors.append("Длина пароля должна быть не менее 8 символов")

    # 2. Хотя бы одна цифра
    if not any(char.isdigit() for char in password):
        errors.append("Пароль должен содержать хотя бы одну цифру")

    # 3. Хотя бы две заглавные буквы
    uppercase_count = sum(1 for char in password if char.isupper())
    if uppercase_count < 2:
        errors.append("Пароль должен содержать хотя бы две заглавные буквы")

    # 4. Хотя бы два различных специальных символа
    special_in_password = set(char for char in password if char in special_symbols)
    if len(special_in_password) < 2:
        errors.append("Пароль должен содержать хотя бы два различных специальных символа из набора: !@#$%^&*")

    # 5. Не должен содержать кириллицу
    if any('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in password):
        errors.append("Пароль не должен содержать символов кириллицы")

    # Вывод результата
    if errors:
        for error in errors:
            print(error)
    else:
        print("Пароль принят")


if __name__ == "__main__":
    task9()