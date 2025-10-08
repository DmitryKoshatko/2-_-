"""
Задание 5
"""
def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    position = int(input("Введите номер буквы (1-26): ")) - 1

    result = ""
    for i in range(4):
        result += alphabet[(position + i) % 26]

    print(result)


if __name__ == "__main__":
    main()