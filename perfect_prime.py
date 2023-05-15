import math

def is_prime(num):
    num = int(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return num > 1

def reversed_is_prime(num):
    return is_prime(int(num[::-1]))

def all_digits_is_prime(num):
    for digit in num:
        if (not is_prime(digit)): return False
    return True

def sum_is_prime(num):
    return sum(int(digit) for digit in num)

for test in range(int(input())):
    num = input()
    
    if is_prime(num) and reversed_is_prime(num) and all_digits_is_prime(num) and sum_is_prime(num):
        print("Yes")
    else:
        print("No")
    
        

