# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(),
# sha1() или любой другой из модуля hashlib задача считается не решённой.

import hashlib


def rabin_karp(s, subs, start):
    assert len(s) > 0 and len(subs) > 0, 'Строки не могут быть пустые'
    assert len(s) > len(subs), 'Подстрока должна быть короче строки'

    len_subs = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(start, len(s) - len_subs + 1):
        if h_subs == hashlib.sha1(s[i:i + len_subs].encode('utf-8')).hexdigest():

            if s[i:i + len_subs] == subs:
                return i

    return -1


def subs_count(s: str, subs: str) -> int:
    start = 0
    count = 0
    len_s = len(s)
    len_subs = len(subs)

    while start < len_s:
        pos = rabin_karp(s, subs, start)
        if pos != -1:
            count += 1
            start = pos + len_subs
        else:
            break

    return count


s_1 = input('Enter string: ')
s_2 = input('Enter substring for searching: ')

n = subs_count(s_1, s_2)
print(f'Substring founded: {n}' if n != 0 else 'Substring not found')
