def task7():
    CORRECT_LOGIN = "admin"
    CORRECT_PASSWORD = "qwerty123"

    login = input("Введите логин: ").strip()
    password = input("Введите пароль: ").strip()

    if not login or not password:
        print("Логин и пароль не могут быть пустыми")
    elif login != CORRECT_LOGIN:
        print("Пользователь не найден")
    elif password != CORRECT_PASSWORD:
        print("Неверный пароль")
    else:
        print("Доступ разрешён")


if __name__ == "__main__":
    task7()