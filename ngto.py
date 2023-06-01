import math

def is_prime(k):
    k = int(k)
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return k > 1

def main():
    for test_num in range(1, int(input()) + 1):
        n = int(input())
        k = 0
        
        for i in range(1, n):
            if math.gcd(n, i) == 1:
                k = k + 1
        
        print('YES' if is_prime(k) else 'NO')    
        
        

if __name__ == '__main__':
    main()
