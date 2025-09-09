def is_prime(num):  # проверка числа на простоту
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes_in_range(a, b): # поиск простых чисел в промежутке
    if a > b:
        a, b = b, a
    if b < 2:
        return []
    if a < 2:
        a = 2

    primes = []
    for i in range(a, b + 1):
        if is_prime(i):
            primes.append(i)
    return primes


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


def check_is_digit(string_output): # проверка ввода на число
    print(string_output, end='')
    num = input("")
    while not num.isdigit():
        num = input("Ошибка, введите число заново: ")
    return int(num)


def action_selection():  # выбор действия
    while True:
        act = input("Введите номер действия: ")
        print("\n" + "-" * 50)

        match act:
            case "1":
                num = check_is_digit("\nВведите число, числа до которого будут проверены: ")
                primes = get_primes_in_range(0, num)
                print(f"\nВот список простых чисел от 0 до {num}: {', '.join(map(str, primes))}")
                print(f"\nВсего простых чисел: {len(primes)}\n")

            case "2":
                n = check_is_digit("\nВведите количество чисел, которые необходимо найти: ")
                result = x_first_prime_number(n)
                print(f"\nВот список {n} первых простых чисел: {', '.join(map(str, result))} \n")

            case "3":
                a = check_is_digit("\nВведите А: ")
                b = check_is_digit("Введите В: ")
                result = get_primes_in_range(a, b)
                print(f"\nВот список простых чисел от {a} до {b}: {', '.join(map(str, result))}")
                print(f"\nВсего чисел в списке: {len(result)}\n")

            case "4":
                num = check_is_digit("\nВведите число для проверки: ")
                if is_prime(num):
                    print(f"\nДа, число {num} является простым\n")
                else:
                    print(f"\nНет, число {num} не является простым\n")

            case "5":
                a = check_is_digit("\nВведите стартовую точку диапазона: ")
                b = check_is_digit("Введите конечную точку диапазона: ")
                print(f"\nСумма простых чисел в диапазоне от {a} до {b}: {sum(get_primes_in_range(a, b))}\n")

            case "0":
                print("\nВыход из программы. До свидания!\n")
                exit()

            case _:
                print("\nОшибка, введите номер действия заново.\n")
                continue   # возвращаемся в начало цикла и ждём правильный ввод

        # если дошли сюда → действие выполнено
        print("-" * 50 + "\n")
        print("Вернемся в главное меню или хотите выйти из программы?")

        while True:
            choice = input("\nВведите номер действия (1 - меню, 0 - выход): ")
            if choice == "0":
                print("\nВыход из программы. До свидания!\n")
                exit()
            elif choice == "1":
                return   # возвращаемся в главное меню
            else:
                print("\nОшибка, введите номер действия заново.")


while True:  # цикл с выводом меню
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

    action_selection()