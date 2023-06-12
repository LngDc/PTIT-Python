for __ in range(int(input())):
    n, p = map(int, input().split())
    
    count = 0
    
    for i in range(p, n+1, p):
        tmp = i
        
        while tmp % p == 0:
            tmp /= p
            count += 1
    
    print(count)