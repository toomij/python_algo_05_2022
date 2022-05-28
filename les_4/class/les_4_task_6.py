import cProfile

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
#        print(f"Test {i} OK")

def fib_loop(n):

    if n < 2:
        return n

    first, second = 0, 1
    for i in range(2, n + 1):
        first, second = second, first + second

    return second


cProfile.run('fib_loop(1000)')

#test_fib(fib_loop)

#  "les_4_task_6.fib_loop(10)"
# 1000 loops, best of 3: 0.836 usec per loop

# "les_4_task_6.fib_loop(100)"
# 1000 loops, best of 3: 4.92 usec per loop

#  "les_4_task_6.fib_loop(500)"
# 1000 loops, best of 3: 38 usec per loop

# "les_4_task_6.fib_loop(5000)"
# 1000 loops, best of 3: 704 usec per loop

