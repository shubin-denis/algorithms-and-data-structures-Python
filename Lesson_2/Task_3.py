# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

n = int(input('Введите натуральное число:'))

revers = 0

while n > 0:
    revers = revers * 10 + n % 10
    n = n // 10

print(f'Обратное число: {revers}')

