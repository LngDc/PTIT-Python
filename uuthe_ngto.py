import math

test = int(input())

def isPrime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return num > 1

for i in range(test):
    string = input()
    
    length = len(string)
    checkLength = isPrime(length)
    
    countPrimeDigit = 0
    for i in string:
        if isPrime(int(i)):
            countPrimeDigit = countPrimeDigit + 1
    countNonPrimeDigit = length - countPrimeDigit
    
    if checkLength and countPrimeDigit > countNonPrimeDigit:
        print("YES")
    else:
        print("NO")
        
