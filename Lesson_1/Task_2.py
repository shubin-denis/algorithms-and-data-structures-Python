
# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.


x = 5
y = 6


# Binary AND

z = 5 & 6
print(f'5 & 6 = {z}')


# Binary OR

z = 5 | 6
print(f'5 | 6 = {z}')


# Binary XOR


z = 5 ^ 6
print(f'5 ^ 6 = {z}')


# Binary Ones Complement
# из-за особенности представления байт

z = ~ x
print(f'~ 5 = {z}')


# Binary Right Shift
# Сдвигает на n знаков вправо, т.е отбрасывает n бит справа.
# равносильно целочисленному делению на 2**n, где n сдвиг.

z = x >> 2
print(f'5 >> 2 = {z}')


# Binary Left Shift
# Сдвигает на n знаков влево, т.е добавляет n бит справа.
# равносильно умножению на 2**n, где n сдвиг.

z = x << 2
print(f'5 >> 2 = {z}')
