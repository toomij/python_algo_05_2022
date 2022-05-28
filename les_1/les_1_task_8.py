# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a <= b <= c or c <= b <= a:
    print(b)
elif b <= a <= c or c <= a <= b:
    print(a)
else:
    print(c)