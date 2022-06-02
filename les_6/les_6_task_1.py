# 1.В диапазоне натуральных чисел от 2 до 99 определить, сколько из
# них кратны каждому из чисел в диапазоне от 2 до 9.
# Урок 6. Работа с динамической памятью
# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

# Python ver: 3.8.9
# OS: macOS-12.4-arm64-arm-64bit
# Arch: ('64bit', '')
# Machine: arm64
# RAM:
# CPU: Apple M1

В первом варианате используется массив. Объем памяти 372 байта.
Во втором варианте используется множества. Объем памяти 876 байта.
В третьем варианте используется словарь по умолчанию. Объем памяти 844 байта.

import sys
from collections import deque
from collections import defaultdict

# Информация о системе:
def my_system_info():
    import platform
    import psutil
    import cpuinfo

    print('Python ver:', platform.python_version())  #
    print('OS:', platform.platform())  #
    print('Arch:', platform.architecture())  #
    print('Machine:', platform.machine())  #
    print('RAM:')
    print('CPU:', cpuinfo.get_cpu_info()['brand_raw'])  #


def show(x):
    summary = 0
    print(f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    summary += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show(key)
                summary += sys.getsizeof(key)
                show(value)
                summary += sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)
                summary += sys.getsizeof(item)
    return f'type={type(summary)}, size={sys.getsizeof(summary)}, obj={summary}\n' \
           f'Объем занятой памяти {summary + sys.getsizeof(summary)} байта.' \


print('*'*50 + ' Вариант 1 '+'*'*50)
# Вариант 1

numbers = [0] * 8
for i in range(2, 100):
    for k in range(2, 10):
        if i % k == 0:
            numbers[k - 2] += 1
i = 0
while i < len(numbers):
    print(f'Числу {i + 2} кратны {numbers[i]} чисел из диапазона от 2 до 99')
    i += 1

print(show(numbers), show(i), show(k), sep='\n')


print('*'*50 + ' Вариант 2 '+'*'*50)

# Вариант 2

numbers = deque()
for i in range(2, 10):
    n = 0
    for k in range(2, 100):
        if k % i == 0:
            n += 1
    numbers.append(n)
    print(f'Числу {i} кратны {numbers[i-2]} чисел из диапазона от 2 до 99')


print(show(numbers))

print('*'*50 + ' Вариант 3 '+'*'*50)

# Вариант 3

numbers = defaultdict(int)
for k in range(2, 10):
    n = 0
    for v in range(2, 100):
        if v % k == 0:
            n += 1
    numbers[k] += n
for k, v in numbers.items():
    print(f'Числу {k} кратны {v} чисел из диапазона от 2 до 99')

print(show(numbers))

# print(my_system_info())