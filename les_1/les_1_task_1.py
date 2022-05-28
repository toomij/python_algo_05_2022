# 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5
print(f'{a} = {bin(a)}')
b = 6
print(f'{b} = {bin(b)}')

#AND
print(f'{a} and {b} = {a & b} ({bin(a & b)})')
# o = a | b

# OR
print(f'{a} or {b} = {a | b} ({bin(a | b)})')

# XOR
print(f'{a} xor {b} = {a ^ b} ({bin(a ^ b)})')

print(f'{a} >> 2 = {a >> 2} ({bin(a >> 2)})')
print(f'{a} << 2 = {a << 2} ({bin(a << 2)})')

# an = a & b
# xo = a ^ b

# a2 = a << 2
# a3 = a >> 2

# print(f'И : {an}')
# print(f'ИЛИ : {o}')
# print(f'XOR : {xo}')
# print(f'<<2 : {a2}')
# print(f'>>2 : {a3}')