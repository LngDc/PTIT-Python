import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return num > 1

def main():
    N, M = map(int, input().split())
    
    C = []
    for i in range(N):
        A = list(map(int, input().split()))
        B = []
        for j in A:
            if is_prime(j):
                B.append(1)
            else: B.append(0)
        C.append(B)
        
    for row in C:
        print(*row)
            

if __name__ == '__main__':
    main()