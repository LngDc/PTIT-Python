def calc(N):
    if N % 2 == 1:
        return sum(1/n for n in range(1, N + 1, 2))
    else:
        return sum(1/n for n in range(2, N + 1, 2))

def main():
    t = int(input())
    while t > 0:
        N = int(input())
        print(f'{calc(N):.6f}')
        
        t -= 1
    

if __name__ == '__main__':
    main()
