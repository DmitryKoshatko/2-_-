"""
Задание 2
"""
print("Вы досмотрели сериал!")

hour = int(input("Сколько часов прошло: "))
minutes = int(input("Сколько минут прошло: "))

print(f'Прошло минут {(hour * 60) + minutes}')
print(f'Часы - {round(float(hour + (minutes / 60)), 2)}')