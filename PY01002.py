string = input()

result = (int)(string[0]) + (int)(string[4]) - (int)(string[8])

if result == 0:
    print("YES")
else:
    print("NO")