# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

def ListCountDivide(list, divide):
    result = 0

    for items in list:
        if items % divide == 0:
            result += 1
    return result

count_2 = 2
count_3 = 3
count_4 = 4
count_5 = 5
count_6 = 6
count_7 = 7
count_8 = 8
count_9 = 9

list_99 = list(range(2, 100))
num_2 = ListCountDivide(list_99, count_2)
num_3 = ListCountDivide(list_99, count_3)
num_4 = ListCountDivide(list_99, count_4)
num_5 = ListCountDivide(list_99, count_5)
num_6 = ListCountDivide(list_99, count_6)
num_7 = ListCountDivide(list_99, count_7)
num_8 = ListCountDivide(list_99, count_8)
num_9 = ListCountDivide(list_99, count_9)

print(f'count by {count_2}: {num_2}')
print(f'count by {count_3}: {num_3}')
print(f'count by {count_4}: {num_4}')
print(f'count by {count_5}: {num_5}')
print(f'count by {count_6}: {num_6}')
print(f'count by {count_7}: {num_7}')
print(f'count by {count_8}: {num_8}')
print(f'count by {count_9}: {num_9}')