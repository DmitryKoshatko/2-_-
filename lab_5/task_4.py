def task4():
    # Исходные данные
    A = {'Москва', 'Тула', 'Рязань', 'Калуга'}
    B = {'Рязань', 'Владимир', 'Калуга', 'Тверь'}
    C = {'Москва', 'Тверь', 'Смоленск', 'Рязань'}
    ALL = {'Москва', 'Тула', 'Рязань', 'Калуга', 'Владимир', 'Тверь', 'Смоленск'}

    print("Компания A обслуживает:", sorted(A))
    print("Компания B обслуживает:", sorted(B))
    print("Компания C обслуживает:", sorted(C))
    print("Все районы страны:", sorted(ALL))
    print()

    # 1. Районы, где есть хотя бы две компании
    districts_two_or_more = set()

    # Проверяем каждый район
    for district in ALL:
        count = 0
        if district in A:
            count += 1
        if district in B:
            count += 1
        if district in C:
            count += 1

        if count >= 2:
            districts_two_or_more.add(district)

    print("1. Районы с хотя бы двумя компаниями:", sorted(districts_two_or_more))

    # 2. Районы, где работает только одна компания
    districts_one_company = set()

    for district in ALL:
        count = 0
        if district in A:
            count += 1
        if district in B:
            count += 1
        if district in C:
            count += 1

        if count == 1:
            districts_one_company.add(district)

    print("2. Районы с одной компанией:", sorted(districts_one_company))

    # 3. Проверка покрытия всех районов
    all_covered = A | B | C
    print("\n3. Все районы, покрытые компаниями:", sorted(all_covered))

    if all_covered == ALL:
        print("✓ Все районы страны покрыты хотя бы одной компанией")
    else:
        uncovered = ALL - all_covered
        print(f"✗ Не покрыты районы: {sorted(uncovered)}")

    # Дополнительно: районы, которые не обслуживаются вообще
    if len(ALL - all_covered) > 0:
        print(f"Необслуживаемые районы: {sorted(ALL - all_covered)}")
    else:
        print("Все районы обслуживаются хотя бы одной компанией")


if __name__ == "__main__":
    task4()