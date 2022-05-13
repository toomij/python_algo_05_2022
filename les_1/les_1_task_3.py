""" 3. Написать программу, которая генерирует в указанных пользователем границах:

a. случайное целое число,

b. случайное вещественное число,

c. случайный символ.

Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
import random

lowLimInt = int(input("Введите целое число нижний границы:\n"))
upLimInt = int(input("Введите целое число верхней границы:\n"))
lowLimReal = float(input("Введите вещественное число для нижней границы:\n"))
upLimReal = float(input("Введите вещественное число для верхней границы:\n"))
lowLimSymb = ord(input("Введите символ для нижней границы:\n"))
upLimSymb = ord(input("Введите символ для верхней границы:\n"))

resIntRand = random.randrange(lowLimInt, upLimInt)
resRealRand = random.uniform(lowLimReal, upLimReal)
resSymbRand = chr(random.randint(lowLimSymb,upLimSymb))

print(f'Случайное целое число: {resIntRand}')
print(f'Случайное вещественое число: {resRealRand}')
print(f'Случайный символ: {resSymbRand}')
