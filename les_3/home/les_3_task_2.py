# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

list_num = [8, 3, 15, 6, 4, 2]
count = len(list_num)

print(count)
print(list_num[0])

list_even = []

for i in range(count):
    if list_num[i] % 2 == 0:
        list_even.append(i)

print(list_even)
