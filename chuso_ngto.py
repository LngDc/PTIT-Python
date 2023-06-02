def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return n > 1

def check(num):
    digits = [int(i) for i in num]
    filtered = list(filter(is_prime, digits))
    
    return is_prime(len(digits)) and len(filtered) > len(digits) - len(filtered)
        

def run():
    if check(input()): print('YES') 
    else: print('NO')
    

def main(func, test_num):
    for i in range(1, test_num + 1):
        func()

if __name__ == '__main__':
    main(run, int(input()))
