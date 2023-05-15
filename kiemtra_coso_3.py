test = int(input())

for i in range(test):
    string = input()
    
    base = "012"
    ok = True
    
    for i in string:
        if i not in base:
            ok = False
            break
    
    if ok:
        print("YES")
    else:
        print("NO")