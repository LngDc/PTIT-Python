test = int(input())

for i in range(test):
    string = input()
    
    if (string[0] == string[-1]):
        print("YES")
    else:
        print("NO")