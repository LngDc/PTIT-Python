test = int(input())

for i in range(test):
    string = input()
    
    length = len(string)
    result = ""
    
    for i in range(0, length - 1, 2):
        char = string[i]
        repeat = int(string[i + 1])
        
        for j in range(repeat):
            result += char
            
    print(result)