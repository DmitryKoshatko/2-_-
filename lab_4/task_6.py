def task6():
    password = input("Введите пароль (только русские буквы): ").lower()

    vowels = "аяоёэеуюыи"
    encrypted = ""

    for char in password:
        if char in vowels:
            encrypted += "0"
        elif char.isalpha():  # проверяем, что это буква (согласная)
            encrypted += "1"
        else:
            encrypted += char  # оставляем другие символы как есть

    print(f"Зашифрованный пароль: {encrypted}")


if __name__ == "__main__":
    task6()