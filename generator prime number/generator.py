def is_prime(num):  # проверка числа на простоту
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_list(a, b):  # все простые числа от a до b включительно (объединено с числами до n)
    if a > b:
        a, b = b, a
        if a < 2:
            a = 2
    elif b == a:
        return []
    else:
        if b < 2:
            return []
    prime_list = []
    for i in range(a, b + 1):
        if is_prime(i):
           prime_list.append(i)
    return prime_list


def x_first_prime_number(x):  # первые x простых чисел
    if x <= 0:
        return []
    list_prime_num = [2]
    num = 3
    while len(list_prime_num) < x:
        if is_prime(num):
            list_prime_num.append(num)
        num += 2
    return list_prime_num


def action_selection(act):  # выбор действия
    print("\n" + "-" * 50)
    match int(act):
        case 1:
            num = int(input("\nВведите число, числа до которого будут проверены: ")) # все простые числа до n включительно
            primes = prime_list(0, num)
            print(f"\nВот список простых чисел от 0 до {num}:\n")
            print(', '.join(map(str, primes)))
            print(f"\nВсего простых чисел: {len(primes)}\n")

        case 2:
            n = int(input("\nВведите количество чисел, которые необходимо найти: ")) # первые n простых чисел
            result = x_first_prime_number(n)
            print(f"\nВот список {n} первых простых чисел:\n")
            print(', '.join(map(str, result)))
            print(f"\nВсего чисел в списке: {len(result)}\n")

        case 3:
            a = int(input("\nВведите А: ")) # все простые числа от a до b включительно
            b = int(input("Введите В: "))
            result = prime_list(a, b)
            print(f"\nВот список простых чисел от {a} до {b}:\n")
            print(', '.join(map(str, result)))
            print(f"\nВсего чисел в списке: {len(result)}\n")

        case 4:
            num = int(input("\nВведите число для проверки: ")) # проверка числа на простоту
            if is_prime(num):
                print(f"\nДа, число {num} является простым\n")
            else:
                print(f"\nНет, число {num} не является простым\n")

        case 5:
            a = int(input("\nВведите стартовую точку диапазона: ")) # сумма простых чисел в диапазоне от a до b включительно
            b = int(input("Введите конечную точку диапазона: "))
            list_num = prime_list(a, b)
            print(f"\nСумма простых чисел в диапазоне от {a} до {b}: {sum(list_num)}\n")

        case _:
            act = input("\nОшибка, введите номер действия заново: ") 
            action_selection(act)

    print("-" * 50 + "\n")
    print("Вернемся в главное меню или хотите выйти из программы?")

    choice = input("\nВведите номер действия (1 - меню, 0 - выход): ")
    if choice == "0":
        print("\nВыход из программы.\n")
        exit()


while True:  #цикл с выводом меню
    print("""
==================================================
Какое действие Вы хотели бы выполнить?
  1. Найти все простые числа до N
  2. Найти N простых чисел
  3. Найти все простые числа от A до B
  4. Узнать, является ли конкретное число простым
  5. Вывести сумму простых чисел в диапазоне
  0. Выйти из программы
==================================================
""")

    act = input("Введите номер действия: ")

    if act == "0":
        print("\nВыход из программы.")
        break

    action_selection(act)