n = int(input('Сколько элементов сложить: '))
item = 1
summa = 0
for i in range(n):
    summa += item
    item /= -2
print(summa)