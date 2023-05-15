test = int(input())

for i in range(test):
    N, d = input().split()
    
    N = int(N)
    d = int(d)
    
    A = input().split()
    B = []
    
    for i in range(d, N):
        B.append(A[i])
        
    for i in range(d):
        B.append(A[i])
        
    print(*B)
