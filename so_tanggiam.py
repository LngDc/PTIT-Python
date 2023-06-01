def check(num):
    digits = [int(digit) for digit in num]
    
    if len(digits) < 3:
        return f'NO'
    
    max_digit = max(digits)
    for i in range(1, digits.index(max_digit) + 1):
        if (digits[i] <= digits[i - 1]):
            return f'NO'
    
    for i in range(digits.index(max_digit) + 1, len(digits)):
        if (digits[i] >= digits[i - 1]):
            return f'NO'
        
    return f'YES'

def main():
    t = int(input())
    
    while t > 0:
        print(check(input()))
        
        t -= 1

if __name__ == '__main__':
    main()
