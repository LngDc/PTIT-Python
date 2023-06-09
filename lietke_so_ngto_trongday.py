def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return n > 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    primes = []
    for i in A:
        if is_prime(i) and i not in primes:
            primes.append(i)
    
    for prime in primes:
        print(f'{prime} {A.count(prime)}')
    
    
    

if __name__ == '__main__':
    main()  