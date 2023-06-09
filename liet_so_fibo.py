def main():
    fibo = [0, 1, 1]
    for i in range(3, 93):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    
    t = int(input())
    while t > 0:
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            print(fibo[i], end = ' ')
        print()
        
        t -= 1

if __name__ == '__main__':
    main()