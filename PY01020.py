test = int(input())

for i in range(test):
    number = input()
    
    if (number[len(number) - 2:] == "86"):
        print("YES")
    else:
        print("NO")