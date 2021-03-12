# В массиве случайных целых чисел поменять местами минимальный и
# максимальный элементы.

import random

arr = [random.randint(0, 99) for _ in range(10)]
# print(arr)

max_index = 0
min_index = 0

for i, n in enumerate(arr):
    if n > arr[max_index]:
        max_index = i
    if n < arr[min_index]:
        min_index = i
arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
print(f'Поменялись местами элементы {min_index} и {max_index}')
print(f'Массив после изменения: {arr}')
