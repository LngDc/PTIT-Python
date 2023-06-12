from itertools import permutations

t = int(input()) + 1
for i in range(1, t):
    a = [int(i) for i in range(1, int(input()) + 1)]
    perms = list(permutations(a))
    perms = perms[::-1]
    print(len(perms))
    for perm in perms:
        print(*perm, sep='', end=' ')
    print()