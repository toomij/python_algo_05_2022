# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

arr = [2, 5, 7, 1, 8]

min_ele, max_ele = arr[0], arr[0]
pos_max = 0
pos_min = 0


for i in range(1, len(arr)):
    if arr[i] < min_ele:
        min_ele = arr[i]
        pos_min = i
    if arr[i] > max_ele:
        max_ele = arr[i]
        pos_max = i

arr[pos_max] = min_ele
arr[pos_min] = max_ele

print('Minimum Element in the list', arr, 'is', min_ele)
print('Maximum Element in the list', arr, 'is', max_ele)
