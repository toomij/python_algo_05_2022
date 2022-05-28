n = int(input('Введите любое натуральное число: '))
left = 0
for i in range(1, n + 1):
    left += i
right = n * (n + 1 ) // 2
print(left)
print(right)
print(left == right)