def check(num):
    if all(int(i) % 2 == 0 for i in num):
        return True
    return False

def main():
    t = int(input())
    for test_num in range(t):
        numbers = []    
        n = int(input())
        
        curr = 2
        
        while curr <= 888:
            if check(str(curr)):
                tmp = str(curr)
                numbers.append(int(str(tmp) + str(tmp)[::-1]))
            curr += 2
    
        for number in numbers:
            if number >= n:
                break
            print(number, end = ' ')
        print()
        

if __name__ == '__main__':
    main()
