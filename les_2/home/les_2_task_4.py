# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

list_str = input("Enter natural number: ")

List1 = [int(x) for x in str(list_str)]

num = int(input("Enter number that count: "))

count = 0

for i in List1:
    if i == num:
        count += 1

print(count)