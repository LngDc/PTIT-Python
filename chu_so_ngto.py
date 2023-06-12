primes = '2357'
res = []

def check(s):
    for p in primes:
        if s.count(p) == 0:
            return False
    return s[-1] != '2'

def Try(i, s, n):
    if i >= 4 and i <= n and check(s):
        res.append(int(s))
    if i < n:
        for p in primes:
            Try(i + 1, s + p, n)

n = int(input())
Try(0, '', n)
print(*sorted(res), sep='\n')
