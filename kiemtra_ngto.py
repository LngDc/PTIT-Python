def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return n > 1

def check(num):
    number = int(num[-4:])
    return 'YES' if is_prime(number) else 'NO'

def solution():
    print(check(input()))
    

def main(sol, test_num):
    for i in range(1, test_num + 1):
        sol()

if __name__ == '__main__':
    main(solution, int(input()))
