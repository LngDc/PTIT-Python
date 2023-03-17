def factorial(n):
    facto = 1
    
    for i in range(1, n + 1):
        facto *= i
        
    return facto

test = int(input())

for i in range(test):
    number = input()
    
    add = 0
    
    for i in number:
        add += factorial(int(i))
        
    if (add == int(number)):
        print("Yes")
    else:
        print("No")
