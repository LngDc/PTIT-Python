test = int(input())

def sumAllEvenPos(string):
    result = 0
    
    for i in range(0, len(string), 2):
        result = result + int(string[i])
        
    return result

def checkAllOddIsZero(string):
    isAllZero = True
    
    for i in range(1, len(string), 2):
        if string[i] != '0':
            isAllZero = False
    
    return isAllZero
            
def multiplyAllOddPos(string):
    result = 1
    
    for i in range(1, len(string), 2):
        if string[i] != '0':
            result = result * int(string[i])
        
    return result
    
for i in range(test):
    string = input()
    
    if checkAllOddIsZero(string):
        print("{} {}".format(sumAllEvenPos(string), 0))
    else:
        print("{} {}".format(sumAllEvenPos(string), multiplyAllOddPos(string)))
    