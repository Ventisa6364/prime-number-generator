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

    match int(act):
        case 1:
            num = int(
                input(
                    "Введите число, до которого включительно будут проверены все числа: "
                )
            )
            print("Вот список простых чисел от 0 до N:", all_prime_to_n(num))

        case 2:
            n = int(input("Введите количество чисел, которые необходимо найти: "))
            result = x_first_prime_number(n)
            print("Вот список N первых простых чисел:", result)
            print("Всего чисел в списке:", len(result))

        case 3:
            a, b = int(input("Введите А:")), int(input("Введите В:"))
            result = all_prime_from_a_to_b(a, b)
            print(f"Вот список простых чисел от {a} до {b}: {result}")
            print("Всего чисел в списке:", len(result))

        case 4:
            num = int(input("Введите число для проверки: "))
            if is_prime(num):
                print(f"Число {num} является простым")
            else:
                print(f"Число {num} не является простым")

        case 5:
            a, b = int(input("Введите стартовую точку диапазона: ")), int(
                input("Введите конечную точку диапазона: ")
            )
            list_num = all_prime_from_a_to_b(a, b)
            print(
                f"Сумма простых чисел в диапазоне от {a} до {b}: {sum(list_num)}"
            )

        case _:
            act = input("Ошибка, введите номер действия заново: ")
            action_selection(act)


print(
    """ Какое действие Вы хотели бы выполнить?
      1. Найти все простые числа до N
      2. Найти N простых чисел
      3. Найти все простые числа от A до B
      4. Узнать, является ли конкретное число простым
      5. Вывести сумму простых чисел в диапазоне
      0. Выйти из программы
"""
)

act = input("Введите номер действия: ")

if act == "0":
        print("Выход из программы.")
else:
    action_selection(act)
