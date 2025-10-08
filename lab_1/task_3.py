"""
Задание 3
"""
def main():
    def translation(seconds):
        if seconds <= 0:
            return 0, 0, 0

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        remaining_seconds = seconds % 60

        return hours, minutes, remaining_seconds


    try:
        seconds = int(input("Введите количество секунд: "))
        if seconds < 0:
            print("Ошибка: количество секунд не может быть отрицательным")
        else:
            hours, minutes, remaining_seconds = translation(seconds)
            print(f"{hours:02d}:{minutes:02d}:{remaining_seconds:02d}")

    except ValueError:
        print("Ошибка: введите целое число")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()