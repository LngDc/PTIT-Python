import math

test = int(input())

def isPrime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return num > 1

for i in range(test):
    string = input()
    firstNum = int(string[0:3])
    secondNum = int(string[len(string) - 3: len(string)])
    
    if isPrime(firstNum) and isPrime(secondNum):
        print("YES")
    else:
        print("NO")
