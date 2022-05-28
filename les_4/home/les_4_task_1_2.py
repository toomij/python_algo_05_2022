# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
import cProfile


def max_below_zero(size):
    array = [random.randint(size * -10, size * 10) for _ in range(size)]

    i = 0
    index = -1

    while i < size:
        if array[i] < 0 and index == -1:
            index = i
        elif array[i] < 0 and array[i] > array[index]:
            index = i

        i += 1

    return f'Число {array[index]} на позиции {index}'
