def main():
    t = int(input())
    
    while t > 0:
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        
        A.sort()
        B.sort()
        
        res = True
        
        for i in range(N):
            if A[i] > B[i]:
                res = False
        
        print('YES' if res else 'NO')
        
        t -= 1
    

if __name__ == '__main__':
    main()