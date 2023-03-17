str = input()

tmp = ""
upper = 0
lower = 0

for x in str:
    tmp += x
    if tmp.islower():
        lower += 1
    else:
        upper += 1
    tmp = ""

if (upper > lower):
    print(str.upper())
else:
    print(str.lower())
