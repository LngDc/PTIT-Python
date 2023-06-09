test = int(input())

for x in range(test):
    string = input() + "a"

    num = ""

    numList = []

    for x in string:
        if x.isdigit():
            num += x
        else:
            numList.append(num)
            num = ""

    while "" in numList:
        numList.remove("")

    max = 0

    for x in numList:
        if int(x) > int(max):
            max = x
            
    print(max)