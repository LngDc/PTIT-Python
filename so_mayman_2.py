
test = (int)(input())

for x in range(test):
    string = input()
    other = "12356890"
    check = True
    
    for x in other:
        if x in string:
            check = False
        
    if check:
        print("YES")
    else:
        print("NO")
        
    