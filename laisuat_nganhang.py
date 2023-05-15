test = int(input())

for i in range(test):
    N, X, M = input().split()
    
    year = 0
    money = float(N)
    
    while money < float(M):
        extra = money * float(X) / 100
        
        money += extra
        
        year += 1
        
    print(year)

