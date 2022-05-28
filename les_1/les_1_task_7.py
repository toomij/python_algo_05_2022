# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input("Enter year: "))

if year % 4 == 0:
    print("Year is leap")
else:
    print("Year is not leap")
