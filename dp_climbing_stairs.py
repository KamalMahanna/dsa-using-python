def clmb(n):
    if n <= 1:
        return 1

    return clmb(n - 1) + clmb(n - 2)


def clmb_mem(n, mem={}):
    if n in mem:
        return mem[n]
    if n <= 1:
        return 1

    mem[n] = clmb_mem(n - 1, mem) + clmb_mem(n - 2, mem)
    return mem[n]


def clmb_tab(n):
    a, b = 0, 1
    for i in range(2, n + 2):
        a, b = b, a + b
    return b


n = 15
print(clmb(n))
print(clmb_mem(n))
print(clmb_tab(n))
