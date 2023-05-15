test = int(input())

for i in range(test):
    number = input()
    
    sum = 0
    cond1 = True
    cond2 = True
    
    for k in range(len(number)):
        sum += int(number[k])
        
        if k == 0: continue
        else:
            if int(number[k]) != int(number[k - 1]) + 2 and int(number[k]) != int(number[k - 1]) - 2:
                cond2 = False
                break
            
    if sum % 10 != 0:
        cond1 = False
        
    if cond1 and cond2:
        print("YES")
    else:
        print("NO")
                
        
        