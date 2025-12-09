def task8():
    email = input("Введите email: ").strip()

    if "@" not in email:
        print("Некорректный email: отсутствует @")
    elif "." not in email.split("@")[-1]:
        print("Некорректный email: отсутствует домен")
    elif email.endswith((".ru", ".com", ".org")):
        print("Email принят")
    else:
        print("Неизвестный домен")


if __name__ == "__main__":
    task8()