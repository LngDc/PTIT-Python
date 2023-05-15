test = int(input())

for i in range(test):
    number = input()
    
    num = sum(int(x) for x in number)
    
    cond1 = True
    cond2 = True
    
    if len(str(num)) < 2:
        cond1 = False
        print("NO")
        break
    
    reverse = str(num)[::-1]
    if int(num) != int(reverse):
        cond2 = False
        print("NO")
        break
    
    print("YES")