"""
Задание 1
"""
def main():
    film = str(input("Введите название фильма: "))
    cinema = str(input("Введите название кинотеатра: "))
    time = str(input("Введите время начала фильма: "))

    print(f'Билет на "{film}" в "{cinema}" на {time} забронирован.')


if __name__ == "__main__":
    main()