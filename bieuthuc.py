t = int(input()) + 1

for i in range(1, t):
    expression = input()
    
    curr_level = 0
    list_level = []
    for character in expression:
        if character == '(':
            curr_level += 1
            list_level.append(curr_level)
            print(curr_level, end=' ')
        if character == ')':
            print(list_level.pop(), end=' ')
    print()