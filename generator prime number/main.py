def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def all_prime_to_n(n):
    if n < 2:
        return []
    prime_list = []
    for num in range(2, n + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list


def all_prime_from_a_to_b(a, b):
    if b < 2 or a > b:
        return []
    prime_list = []
    for num in range(a, b + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list


def x_first_prime_number(x):
    list_prime_num = []
    num = 2
    while len(list_prime_num) < x:
        if is_prime(num):
            list_prime_num.append(num)
        num += 1
    return list_prime_num


def action_selection(act):
    print("\n" + "-" * 50)
    match int(act):
        case 1:
            num = int(
                input(
                    "\nВведите число, числа до которого будут проверены: "
                )
            )
            primes = all_prime_to_n(num)
            print("\nВот список простых чисел от 0 до N:\n")
            print(primes)
            print(f"\nВсего простых чисел: {len(primes)}")

        case 2:
            n = int(input("\nВведите количество чисел, которые необходимо найти: "))
            result = x_first_prime_number(n)
            print("\nВот список N первых простых чисел:\n")
            print(result)
            print(f"\nВсего чисел в списке: {len(result)}")

        case 3:
            a = int(input("\nВведите А: "))
            b = int(input("Введите В: "))
            result = all_prime_from_a_to_b(a, b)
            print(f"\nВот список простых чисел от {a} до {b}:\n")
            print(result)
            print(f"\nВсего чисел в списке: {len(result)}")

        case 4:
            num = int(input("\nВведите число для проверки: "))
            if is_prime(num):
                print(f"\nЧисло {num} является простым")
            else:
                print(f"\nЧисло {num} не является простым")

        case 5:
            a = int(input("\nВведите стартовую точку диапазона: "))
            b = int(input("Введите конечную точку диапазона: "))
            list_num = all_prime_from_a_to_b(a, b)
            print(f"\nСумма простых чисел в диапазоне от {a} до {b}: {sum(list_num)}")

        case _:
            act = input("\nОшибка, введите номер действия заново: ")
            action_selection(act)
    print("-" * 50 + "\n")


while True:
    print(
        """
==================================================
Какое действие Вы хотели бы выполнить?
  1. Найти все простые числа до N
  2. Найти N простых чисел
  3. Найти все простые числа от A до B
  4. Узнать, является ли конкретное число простым
  5. Вывести сумму простых чисел в диапазоне
  0. Выйти из программы
==================================================
"""
    )

    act = input("Введите номер действия: ")

    if act == "0":
        print("\nВыход из программы.")
        break

    action_selection(act)
