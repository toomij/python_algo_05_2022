# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

# вариант 1
num = int(input('Введите число: '))
result = 0
while num > 0:
    result = result * 10 + num % 10
    num = num // 10
print(result)

# вараинт 3
num = input('Введите число: ')
result = ''
result = num[::-1]
print(result)


# вариант 4
# list_str = input("Enter natural number: ")
#
# list1 = [int(x) for x in str(list_str)]
#
# list2 = []
#
# range_list = len(list1) - 1
#
# for i in list1:
#     list2.append(list1[range_list])
#     range_list -= 1
#
# print(list2)