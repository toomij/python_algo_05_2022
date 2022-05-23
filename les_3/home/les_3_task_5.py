# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

SIZE = 10
array = [random.randint(-100, 100) for _ in range(SIZE)]
print(array)

i = 0
index = -1

while i < SIZE:
    if array[i] < 0 and index == -1:
        index = i
    elif 0 > array[i] > array[index]:
        index = i

    i += 1

print(f'Число {array[index]} на позиции {index}')

# def MaxElem(list1):
#     maxelement = list1[0]
#     for element in list1:
#         if element > maxelement:
#             maxelement = element
#     return maxelement
#
#
# l=[-5, -6, -5, -60, -32 ]
# result = MaxElem(l)
# print(result)