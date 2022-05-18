# Algorythm Evklida

def gcd1(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m


def gcd2(m, n):
    if n == 0:
        return m
    return gcd2(n, m % n)


print(gcd1(54, 24))
print(gcd2(54, 24))
