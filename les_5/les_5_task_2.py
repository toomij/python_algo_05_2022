# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
#
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
#
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
# задача решается в несколько строк.
# Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
#
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

from collections import deque

# Variant 1
# def add_hex(A, B):
#     A = "0"+A
#     B = "0"+B
#     #Remember all pattern include carry in variable d.
#     i2h = dict(zip(range(16), "0123456789abcdef"))
#     a = [(i,j) for i in "0123456789abcdef" for j in "0123456789abcdef"]
#     b = list(map(lambda t: int(t[0],16)+int(t[1],16), a))
#     c = ["0"+i2h[i] if i<16 else "1"+i2h[i-16] for i in b]#list of digit include carry
#     d = dict(zip(a,c))#d={(digit,digit):digit,,,}
#     #Calculate with variable d.
#     result = ""
#     cur = "0"
#     nex = "0"
#     for i in itertools.zip_longest(A[::-1], B[::-1], fillvalue = "0"):
#         cur = d[(nex, d[i][1])][1]                   #cur = carry + digit + digit
#         if d[i][0]=='1' or d[(nex, d[i][1])][0]=='1':#nex = carry = carry + digit + digit
#             nex = "1"
#         else:
#             nex = "0"
#         result += cur
#
#     return result[::-1]

# Variant 2
def add_hex(x, y):

    list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    if len(x) > len(y):
       x, y = y, x
    y = y[::-1]
    result = []

    j = -1
    k = 0
    for i in y:
        one = list_of_numbers.index(i)
        two = list_of_numbers.index(x[j])
        result.append(list_of_numbers[(one + two + k) % 16])
        if (one + two) >= 15:
            k = 1
        else:
            k = 0
        j -= 1
        if j == -len(x) - 1:
            break

    diff = len(y) - len(x)

    if diff:
        for i in y[-diff:]:
            result.append(list_of_numbers[(list_of_numbers.index(i) + k) % 16])
            if list_of_numbers.index(y[-diff]) + 1 >= 15:
                k = 1
            else:
                k = 0
    if k == 1:
        result.append('1')

    return result[::-1]


def mult_hex(x, y):
    HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,\
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, \
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', \
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    result = deque()
    temp = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = HEX_NUM[y.pop()]

        for j in range(len(x) - 1, -1, -1):
            temp[i].appendleft(m * HEX_NUM[x[j]])

        for _ in range(i):
            temp[i].append(0)

    transfer = 0

    for _ in range(len(temp[-1])):
        res = transfer

        for i in range(len(temp)):
            if temp[i]:
                res += temp[i].pop()

        if res < 16:
            result.appendleft(HEX_NUM[res])
        else:
            result.appendleft(HEX_NUM[res % 16])
            transfer = res // 16

    if transfer:
        result.appendleft(HEX_NUM[transfer])

    return list(result)

#Test

#A = "A2"
#B = "C4F"
#print(hex(int(A,16)+int(B,16))) #For validation

a = list(input('Enter first HEX number: ').upper())
b = list(input('Enter second HEX number: ').upper())

print(*a, '+', *b, '=', *add_hex(a, b))

print(*a, '*', *b, '=', *mult_hex(a, b))