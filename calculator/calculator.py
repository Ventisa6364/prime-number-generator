def action_selection(act):
    print("\n" + "-" * 50)
    match int(act):
        case 1:
            num1 = float(input("\nВведите первое число: "))
            num2 = float(input("Введите второе число: "))
            print(f"\nРезультат: {num1} + {num2} = {num1 + num2}\n")
        case 2:
            num1 = float(input("\nВведите первое число: "))
            num2 = float(input("Введите второе число: "))
            print(f"\nРезультат: {num1} - {num2} = {num1 - num2}\n")
        case 3:
            num1 = float(input("\nВведите первое число: "))
            num2 = float(input("Введите второе число: "))
            print(f"\nРезультат: {num1} * {num2} = {num1 * num2}\n")
        case 4:
            num1 = float(input("\nВведите первое число: "))
            num2 = float(input("Введите второе число: "))
            print(f"\nРезультат: {num1} / {num2} = {num1 / num2}\n")
        case 5:
            num1 = float(input("\nВведите основание степени: "))
            num2 = float(input("Введите степень: "))
            print(f"\nРезультат: {num1} ** {num2} = {num1 ** num2}\n")
        case 6:
            num = float(input("\nВведите число для вычисления квадратного корня: "))
            degree = float(input("Введите степень корня (по умолчанию 2): ") or 2)
            print(f"\nРезультат: {degree}√{num} = {num ** (1 / degree)}\n")
        case _:
            print(
                "\nНекорректный ввод. Пожалуйста, выберите действие из списка и введите его номер: \n"
            )


while True:
    print(
        """
==================================================
Какое действие Вы хотели бы выполнить?
  1. Сложение
  2. Вычитание
  3. Умножение
  4. Деление
  5. Возведение в степень
  6. Квадратный корень (или корень другой степени)
  0. Выйти из программы
==================================================
"""
    )

    act = input("Введите номер действия: ")

    if act == "0":
        print("\nВыход из программы.")
        break

    action_selection(act)
