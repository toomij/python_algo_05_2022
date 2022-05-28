# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

# вариант 1
num = int(input("Введите количество чисел: "))
digit = int(input("Какую цифру посчитать?: "))
count = 0
for i in range(1, num + 1):
    m = int(input(f'Введите число {i}: '))
    while m > 0:
        if m % 10 == digit:
            count += 1
        m = m // 10
print(f'Было введено {count} цифр {digit}')

# list_str = input("Enter natural number: ")
#
# List1 = [int(x) for x in str(list_str)]
#
# num = int(input("Enter number that count: "))
#
# count = 0
#
# for i in List1:
#     if i == num:
#         count += 1
#
# print(count)