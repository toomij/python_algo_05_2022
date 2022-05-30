# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

list_str = input("Enter natural number: ")

list1 = [int(x) for x in str(list_str)]

odd_count = len(list(filter(lambda x: (x % 2 != 0), list1)))

# we can also do len(list1) - odd_count
even_count = len(list(filter(lambda x: (x % 2 == 0), list1)))

print("Even numbers in the input: ", even_count)
print("Odd numbers in the input: ", odd_count)