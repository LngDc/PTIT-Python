test = int(input())

for i in range(test):
    string = input()
    string += " "
    
    length = len(string)
    currChar = string[0]
    count = 1
    result = ""
    
    for j in range(1, length):
        if string[j] == currChar:
            count += 1
        else:
            result += str(count)
            result += currChar
            currChar = string[j]
            count = 1
            
    print(result)
            