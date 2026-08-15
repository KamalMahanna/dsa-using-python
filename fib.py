def fib(n, mem={}):
    if n in mem:
        return mem[n]
    if n <= 1:
        return n
    mem[n] = fib(n - 1, mem) + fib(n - 2, mem)
    return mem[n]


def fib_2(n):
    if n <= 1:
        return n
    return fib_2(n - 1) + fib_2(n - 2)


def dp_tab(n):
    a = 0
    b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


from time import time

n = 40
st_ = time()
print(fib_2(n))
print(time() - st_)

st_ = time()
print(fib(n))
print(time() - st_)

st_ = time()
print(dp_tab(n))
print(time() - st_)
