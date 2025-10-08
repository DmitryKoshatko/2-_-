"""
Задание 6
"""
def main():
    word = input("Введите слово: ")

    print(f"Результат: {word[((len(word)) - 1) // 2]}")


if __name__ == "__main__":
    main()