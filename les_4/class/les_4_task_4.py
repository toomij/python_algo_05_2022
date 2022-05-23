import cProfile

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
       # print(f"Test {i} OK")

def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]

        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)

cProfile.run('fib_dict(100)')

# 1000 loops, best of 3: 6.5 usec per loop

#"les_4_task_4.fib_dict(20)"
# 1000 loops, best of 3: 8.41 usec per loop

# "les_4_task_4.fib_dict(100)"
# 1000 loops, best of 3: 44.7 usec per loop