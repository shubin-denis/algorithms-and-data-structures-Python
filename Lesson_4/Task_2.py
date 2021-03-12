# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте
# его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

from timeit import timeit
# 1) Алгоритм «Решето Эратосфена».


def sieve_it(n):
    primes = [i for i in range(0, n)]
    primes[0] = 0
    primes[1] = 0

    for i in range(1, n):
        if primes[i] != 0:
            j = i + i
            while j < n:
                primes[j] = 0
                j += i
    return primes


def sieve(n):
    if n == 1:
        return 2
    lim = n
    primes_found = 0
    while primes_found < n:
        lst = sieve_it(lim)
        for num in lst:
            if num != 0:
                primes_found += 1
            if primes_found == n:
                return num
        lim *= 2
        primes_found = 0


# 2) Поочередная проверка каждого числа на простоту
def prime(n):
    x = 1
    primes = [2]  #
    while len(primes) < n:
        x += 2
        for i in primes:
            if x % i == 0:
                break
        else:
            primes.append(x)
    return primes[-1]


# Тестируем время выполнения функцией
def test(func, values):
    for i in values:
        time = timeit('func(var)', number=100, globals={'func': func, 'var': i})
        print(f'{func.__name__}({i}): {time:.6f}')


if __name__ == '__main__':
    rng = [2 ** i * 5 for i in range(1, 12)]

    test(sieve, rng)
    print()
    test(prime, rng)


# sieve(10): 0.002396
# sieve(20): 0.003805
# sieve(40): 0.017245
# sieve(80): 0.037394
# sieve(160): 0.080563
# sieve(320): 0.214576
# sieve(640): 0.389020
# sieve(1280): 1.521919
# sieve(2560): 3.545443
# sieve(5120): 6.987406
# sieve(10240): 14.838725

# prime(10): 0.000613
# prime(20): 0.001922
# prime(40): 0.007091
# prime(80): 0.022606
# prime(160): 0.084291
# prime(320): 0.332123
# prime(640): 1.302948
# prime(1280): 5.200024
# prime(2560): 21.554081
# prime(5120): 121.397821
# prime(10240): 617.796013