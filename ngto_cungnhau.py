import math

def main():
    N, K = map(int, input().split())
    
    L = 10 ** (K - 1)
    R = 10 ** K
    
    res = []
    for i in range(L, R):
        if math.gcd(i, N) == 1:
            res.append(i)
    
    count = 0
    for i in res:
        print(i, end = ' ')
        count += 1
        
        if count == 10:
            print()
            count = 0
            

if __name__ == '__main__':
    main()
