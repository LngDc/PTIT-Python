from collections import Counter

def main():
    t = int(input())
    while t:
        n, m, k = map(int, input().split())
        A = Counter(list(map(int, input().split())))
        B = Counter(list(map(int, input().split())))
        C = Counter(list(map(int, input().split())))
        
        res = list((A & B & C).elements())
        if len(res) == 0:
            print('NO')
        else:
            print(*res)
        
        
        t -= 1

if __name__ == '__main__':
    main()