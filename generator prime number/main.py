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
    if b < 2:
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


def sum_nums_in_list(list_prime_num):

    sum_nums = 0

    for i in list_prime_num:
        sum_nums += i

    return sum_nums


print(
    """ Какое действие Вы хотели бы выполнить?
      1. Найти все простые числа до N
      2. Найти N простых чисел
      3. Найти все простые числа от A до N
      4. Узнать, является ли конкретное число простым
      5. Вывести сумму простых чисел в диапазоне
"""
)

act = input("Введите номер действия: ")


def action_selection(act):

    match int(act):
        case 1:
            num = int(
                input(
                    "Введите число, до которого включительно будут проверены все числа: "
                )
            )
            print(all_prime_to_n(num))

        case 2:
            n = int(input("Введите количество чисел, которые необходимо найти: "))
            print(x_first_prime_number(n))

        case 3:
            a, b = int(input("Введите А:")), int(input("Введите В:"))
            print(all_prime_from_a_to_b(a, b))

        case 4:
            num = int(input("Введите числло для проверки: "))
            print(is_prime(num))

        case 5:
            a, b = int(input("Введите стартовую точку диапазона: ")), int(
                input("Введите конечную точку диапазона: ")
            )
            list_num = all_prime_from_a_to_b(a, b)
            print(sum_nums_in_list(list_num))

        case _:
            act = input("Ошибка, введите номер действия заново: ")
            action_selection(act)
