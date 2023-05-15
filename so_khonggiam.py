test = int(input())

for i in range(test):
    number = input()
    
    ok = True
    length = len(number)
    prev = int(number[0])
    curr = int(number[0])
    
    for j in range(1, length):
        curr = int(number[j])
        
        if curr < prev:
            ok = False
            break
    
    if ok:
        print("YES")
    else:
        print("NO")