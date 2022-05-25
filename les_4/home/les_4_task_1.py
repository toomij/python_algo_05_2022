# -*- coding: utf-8 -*-

# TODO: 1. Проанализировать скорость и сложность
#  одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
#
# Примечание. Идеальным решением будет:
#
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
#
# b. написать 3 варианта кода (один у вас уже есть),
#
# c. проанализировать 3 варианта и выбрать оптимальный,
#
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
#
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random
import numpy as np

# вариант 1

def neg_one(n):
    array = [random.randint(-100, 100) for _ in range(n)]

    i = 0
    index = -1

    while i < n:
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i

        i += 1
    return array[index]
    # print(f'Число {array[index]} на позиции {index}')


# вариант 2

def neg_two(n):
    SIZE = n
    array = [random.randint(-100, 100) for _ in range(SIZE)]

    num = float('-inf')
    index = -1

    for i, item in enumerate(array):
        if 0 > item > num:
            num = item
            index = i

    # print(f'Число {num} на позиции {index}')


# вариант 3
def neg_three(n):

    array = [random.randint(-100, 100) for _ in range(n)]
    #return array
    return [i for i in array if i < 0]
    #return max([i for i in array if i < 0])

#print(neg_three(10))

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.neg_one(5)"
# 1000 loops, best of 3: 8.09 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.neg_one(10)"
# 1000 loops, best of 3: 13.7 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.neg_one(100)"
# 1000 loops, best of 3: 128 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.neg_one(1000)"
# 1000 loops, best of 3: 1.25 msec per loop

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.neg_two(5)"
# 1000 loops, best of 3: 7.18 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.neg_two(10)"
# 1000 loops, best of 3: 13 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.neg_two(100)"
# 1000 loops, best of 3: 124 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.neg_two(1000)"
# 1000 loops, best of 3: 1.19 msec per loop

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.neg_three(5)"
# 1000 loops, best of 3: 6.74 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.neg_three(10)"
# 1000 loops, best of 3: 12.9 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.neg_three(100)"
# 1000 loops, best of 3: 122 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.neg_three(1000)"
# 1000 loops, best of 3: 1.19 msec per loop
