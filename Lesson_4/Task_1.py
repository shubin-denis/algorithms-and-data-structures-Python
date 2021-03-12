# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

import timeit
import cProfile


def test_prime(func):
    lst = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def summa1(n):
    if n == 0:
        return 0
    return n + summa1(n - 1)


def summa2(n):
    spam_sum = 0
    for i in range(n+1):
        spam_sum += i
    return spam_sum


def summa3(n):
    return n * (n + 1) // 2


# test_prime(summa1)
# test_prime(summa2)
# test_prime(summa3)

# print(timeit.timeit('summa1(10)', number=100, globals=globals()))  # 0.0001905999999999991
# print(timeit.timeit('summa1(20)', number=100, globals=globals()))  # 0.0003382999999999997
# print(timeit.timeit('summa1(100)', number=100, globals=globals()))  # 0.00184440000000001
# print(timeit.timeit('summa1(300)', number=100, globals=globals()))  # 0.007024599999999992
# print(timeit.timeit('summa1(990)', number=100, globals=globals()))  # 0.02504089999999999
#
# print(timeit.timeit('summa2(10)', number=100, globals=globals()))  # 0.0001588000000000006
# print(timeit.timeit('summa2(20)', number=100, globals=globals()))  # 0.00023980000000001223
# print(timeit.timeit('summa2(100)', number=100, globals=globals()))  # 0.0008052000000000059
# print(timeit.timeit('summa2(300)', number=100, globals=globals()))  # 0.001676800000000006
# print(timeit.timeit('summa2(990)', number=100, globals=globals()))  # 0.005114200000000013
#
# print(timeit.timeit('summa3(10)', number=100, globals=globals()))  # 2.340000000000675e-05
# print(timeit.timeit('summa3(20)', number=100, globals=globals()))  # 2.0499999999992746e-05
# print(timeit.timeit('summa3(100)', number=100, globals=globals()))  # 2.1099999999996122e-05
# print(timeit.timeit('summa3(300)', number=100, globals=globals()))  # 2.340000000000675e-05
# print(timeit.timeit('summa3(990)', number=100, globals=globals()))  # 2.289999999999237e-05


# cProfile.run('summa1(100_000)')

   #       996 function calls (4 primitive calls) in 0.004 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.004    0.004 <string>:1(<module>)
   #  993/1    0.004    0.000    0.004    0.004 Task_1.py:12(summa1)
   #      1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('summa2(100_000)')

   #       4 function calls in 0.007 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.007    0.007 <string>:1(<module>)
   #      1    0.007    0.007    0.007    0.007 Task_1.py:18(summa2)
   #      1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('summa3(100_000)')

   #       4 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 Task_1.py:25(summa3)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# При любых n вычисление по формуле будет быстрее, чем рекурсивно и циклом.
