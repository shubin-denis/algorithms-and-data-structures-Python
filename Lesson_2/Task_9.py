# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

n = int(input('Введите количество обрабатываемых чисел: '))
i = 1
max_sum = 0
while i <= n:
    sum_num = 0
    number = int(input('Введите обрабатываемое число: '))
    num = int(number)
    i += 1
    for j in range(len((str(number)))):
        sum_num += num % 10
        num //= 10
    if sum_num > max_sum:
        max_sum = sum_num
        max_num = number
        print(f'Число {max_num} имеет наибольшую сумму цифр - {max_sum}')
