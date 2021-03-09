# В одномерном массиве целых чисел определить два наименьших
# элемента. Они могут быть как равны между собой (оба являться
# минимальными), так и различаться.

import random

arr = [random.randint(0, 99) for _ in range(100)]
# print(arr)

# Простой способ

s_list = []
s_list.extend(arr)
s_list.sort()

print(f'Два наименьших числа: {s_list[0]} и {s_list[1]}')

# Через цикл for

index_1 = 0
index_2 = 1

for i in arr:
    if arr[index_1] > i:
        index_2 = index_1
        index_1 = arr.index(i)
    elif arr[index_2] > i:
        index_2 = arr.index(i)

print(f'Два наименьших числа: {arr[index_1]} и {arr[index_2]}')



