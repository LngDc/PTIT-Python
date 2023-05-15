import math

test = int(input())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(test):
    num = input()
    digits = [int(d) for d in num]
    even_digits = digits[0::2]
    odd_digits = digits[1::2]
    
    if any(digit % 2 == 0 for digit in odd_digits) or any(digit % 2 == 1 for digit in even_digits):
        print("NO")
        continue
    
    digits_sum = sum(digits)
    if not is_prime(digits_sum):
        print("NO")
        continue
    
    print("YES")