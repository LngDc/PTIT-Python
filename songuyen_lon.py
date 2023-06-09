import math

def find_lcd(a, b):
    return math.gcd(a, b)

for test in range(int(input())):
    first = int(input())
    second = int(input())
    
    print(find_lcd(first, second))