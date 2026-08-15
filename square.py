
def perf_sqrt(n):
    if n in [0,1]:
        return True
    l=0
    r=n
    while l<r:
        m=(l+r)//2
        sq = m**2
        if sq == n:
            return True
        elif sq<n:
            l=m+1
        else:
            r=m-1
    return False

print(perf_sqrt(1))
print(perf_sqrt(2))
print(perf_sqrt(3))
print(perf_sqrt(216))
print(perf_sqrt(5801570736025))
