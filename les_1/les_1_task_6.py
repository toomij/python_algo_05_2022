# 6. По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника,
# составленного из этих отрезков.
# Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.


print("Стороны:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("The triangle exists")
    if a == b and b == c and c == a:
        print("The triangle is equilateral")
    else:
        if a == b and b == a or b == a and b == c or c == a and c == b:
            print("The triangle is isosceles")
        else:
            print("The triangle is versatile")
else:
    print("The triangle doesn't exist")