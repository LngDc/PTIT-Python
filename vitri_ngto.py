def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return n > 1

def check(num):
    primes = ['2', '3', '5', '7']
    
    idx_prime = [idx for idx in range(len(num)) if is_prime(idx)]
    idx_non_prime = [idx for idx in range(len(num)) if idx not in idx_prime]
    
    return 'NO' if any(num[idx] not in primes for idx in idx_prime) or any(num[idx] in primes for idx in idx_non_prime) else 'YES'
    

def solution():
    num = input()
    print(check(num))
    

def main(func, t):
    for i in range(1, t + 1):
        func()

if __name__ == '__main__':
    main(solution, int(input()))