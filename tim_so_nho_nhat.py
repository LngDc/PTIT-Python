test = int(input())

for x in range(test):
    string = input()

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

    min = int(numList[0])

    for x in numList:
        if int(x) < int(min):
            min = x
            
    print(min)