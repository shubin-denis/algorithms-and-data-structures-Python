# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

while True:
    question = input('Хотите ввести числа (y / n)? ')
    if question == 'n':
        print('Всего доброго!')
        break
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    operator = input('Введите знак операции (+, -, *, /): ')
    if operator == '+':
        print(f'Сумма чисел: {a + b}')
    elif operator == '-':
        print(f'Разница чисел: {a - b}')
    elif operator == '*':
        print(f'Произведение чисел: {a * b}')
    elif operator == '/':
        if int(b) == 0:
            print('Делить на ноль нельзя!!!')
        else:
            print(f'Деление чисел: {round(a / b, 2)}')
    else:
        print('Неверный знак операции!')


