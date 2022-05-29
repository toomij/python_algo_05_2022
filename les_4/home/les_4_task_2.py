# -*- coding: utf-8 -*-
#TODO: 2. Написать два алгоритма нахождения i-го по счёту простого числа.
#  Функция нахождения простого числа должна принимать
#  на вход натуральное и возвращать соответствующее простое число.
#  Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
#
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
#
# Примечание. Вспомните классический способ проверки числа на простоту.
#
# Пример работы программ:
#
#     >>> sieve(2)
#     3
#     >>> prime(4)
#     7
#     >>> sieve(5)
#     11
#     >>> prime(1)
#     2
# Примечание по профилированию кода: для получения достоверных результатов при замере времени необходимо
# исключить/заменить функции print() и input() в анализируемом коде.
# С ними вы будете замерять время вывода данных в терминал и время, потраченное пользователем, на ввод данных,
# а не быстродействие самого алгоритма.

# Решето Эратосфена
import cProfile

def sieve(n):

    #n = int(input('До какого числа получать простые числа: '))

    sieve = [i for i in range(n)]
    sieve[1] = 0


    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i


    result = [i for i in sieve if i != 0]
    #print(result)
    return result

def prime(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1
        #for i in range(2, current_prime):
        for i in range(2, int(current_prime ** 0.5) + 1):
            if current_prime % i == 0:
                break
        else:
            count += 1
    return current_prime


cProfile.run('prime(1000)')
#sieve(6)
#prime(6)

# if __name__ == '__main__':
#     import timeit
#     print(timeit.timeit("sieve(6)", setup="from __main__ import sieve"))
#     print(timeit.timeit("prime(6)", setup="from __main__ import prime"))

# 2.038340146 print(timeit.timeit("sieve(6)", setup="from __main__ import sieve"))
# 3.10190431 print(timeit.timeit("prime(6)", setup="from __main__ import prime"))


# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(5)"
# 1000 loops, best of 3: 1.9 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(10)"
# 1000 loops, best of 3: 2.87 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(100)"
# 1000 loops, best of 3: 22 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(5)"
# 1000 loops, best of 3: 2.63 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(10)"
# 1000 loops, best of 3: 7.85 usec per loop
#  python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(100)"
# 1000 loops, best of 3: 289 usec per loop

# 6 function calls in 0.000 seconds cProfile.run('sieve(5)')
# 6 function calls in 0.000 seconds cProfile.run('sieve(10)')
# 6 function calls in 0.000 seconds cProfile.run('sieve(100)')
# 6 function calls in 0.000 seconds cProfile.run('sieve(1000)')


# 6 function calls in 0.000 seconds cProfile.run('prime(5)')
# 8 function calls in 0.000 seconds cProfile.run('prime(10)')

# 29 function calls in 0.001 seconds cProfile.run('prime(100)')
# 172 function calls in 0.017 seconds Profile.run('prime(1000)')