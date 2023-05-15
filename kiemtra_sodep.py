test = int(input())

for i in range(test):
    number = input()
    
    numList = set()
    cond1 = True
    cond2 = True
    
    for x in number:
        numList.add(x)
        
        if (len(numList) > 2):
            cond1 = False
            break
        
        first = number[0]
        second = number[1]
        length = len(number)
        
        for j in range(2, length, 2):
            if number[j] != first:
                cond1 = False
                break
        
        for j in range(3, length, 2):
            if (number[j] != second):
                cond2 = False
                break
        
    if cond1 and cond2:
        print("YES")
    else:
        print("NO")
            