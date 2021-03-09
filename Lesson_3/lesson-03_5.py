# В массиве найти максимальный отрицательный элемент. Вывести на
# экран его значение и позицию в массиве.

import random

arr = [random.randint(-99, 99) for _ in range(100)]
# print(arr)

min_index = 0

for i in arr:
    if arr[min_index] > i:
        min_index = arr.index(i)
        print(min_index)

print(f'Минимальный отрицательный элемент: {arr[min_index]}.Находится на позиции {min_index}')
