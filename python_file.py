string = input().lower()

if (len(string) >= 3):
    if string[-3:] != ".py":
        print("no")
    else:
        print("yes")
else:
    print("no")