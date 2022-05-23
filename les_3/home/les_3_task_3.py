# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
array = [random.randint(-100, 100) for _ in range(SIZE)]

# 1 Variant
idx_min = 0
idx_max = 0

for i in range(SIZE):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i

print(f'Min = {array[idx_min]} в ячейке {idx_min}'
      f'\nMax = {array[idx_max]} в ячейке {idx_max}')

array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)





# arr = [2, 5, 7, 1, 8]
#
# min_ele, max_ele = arr[0], arr[0]
# pos_max = 0
# pos_min = 0
#
#
# for i in range(1, len(arr)):
#     if arr[i] < min_ele:
#         min_ele = arr[i]
#         pos_min = i
#     if arr[i] > max_ele:
#         max_ele = arr[i]
#         pos_max = i
#
# arr[pos_max] = min_ele
# arr[pos_min] = max_ele
#
# print('Minimum Element in the list', arr, 'is', min_ele)
# print('Maximum Element in the list', arr, 'is', max_ele)
