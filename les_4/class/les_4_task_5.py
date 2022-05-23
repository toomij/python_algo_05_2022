import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        #print(f"Test {i} OK")


def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_l[n]

    return _fib_list(n)


cProfile.run('fib_list(500)')
# 19/1    0.000    0.000    0.000    0.000 les_4_task_5.py:15(_fib_list) 10
# 39/1    0.000    0.000    0.000    0.000 les_4_task_5.py:15(_fib_list) 20
# 199/1    0.000    0.000    0.000    0.000 les_4_task_5.py:15(_fib_list) 100
# 999/1    0.001    0.000    0.001    0.001 les_4_task_5.py:15(_fib_list)

#test_fib(fib_list)

# "les_4_task_5.fib_list(10)"
# 1000 loops, best of 3: 9.28 usec per loop

# "les_4_task_5.fib_list(20)"
# 1000 loops, best of 3: 10.7 usec per loop

# "les_4_task_5.fib_list(100)"
# 1000 loops, best of 3: 41 usec per loop

#  "les_4_task_5.fib_list(200)"
# 1000 loops, best of 3: 85.7 usec per loop

# "les_4_task_5.fib_list(500)"
# 1000 loops, best of 3: 227 usec per loop
