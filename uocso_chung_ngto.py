import math

def is_prime(k):
    k = int(k)
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return k > 1

def main():
    for test_num in range(1, int(input()) + 1):
        num_1, num2 = [int(i) for i in input().split()]
        gcd = math.gcd(num_1, num2)
        print('YES' if is_prime(sum([int(i) for i in str(gcd)])) else 'NO')   
        
        

if __name__ == '__main__':
    main()
