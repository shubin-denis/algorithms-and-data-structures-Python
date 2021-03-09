# Определить, какое число в массиве встречается чаще всего

import random

arr = [random.randint(0, 99) for _ in range(100)]
# print(arr)


max_index = 0

for i in arr:
    if arr.count(max_index) < arr.count(i):
        max_index = arr.index(i)

print(f'Число {arr[max_index]} встречается {arr.count(max_index)} раза')
