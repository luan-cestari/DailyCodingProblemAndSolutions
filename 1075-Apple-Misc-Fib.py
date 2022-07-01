
def given_n_calculate_fib_space_O_1(n):
    '''Calculate the nth number of fibonnaci sequence'''
    t1 = 0
    t2 = 1

    if n == 1:
        return t1

    if n == 2:
        return t2

    n -= 2

    t3 = 0
    while n > 0:
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        n -= 1
    return t3


n = int(input())
print(given_n_calculate_fib_space_O_1(n))
