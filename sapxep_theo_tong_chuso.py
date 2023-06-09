def calc_sum(n):
    return sum([int(i) for i in n])

def main():
    t = int(input())
    while t > 0:
    
        N = int(input())
        A = input().split()
        
        pairs = {}
        for i in A:
            pairs[i] = calc_sum(i)
            
        A = sorted(A, key=lambda x: (pairs[x], int(x)))
        print(*A)
        
        t -= 1

    
    
    

if __name__ == '__main__':
    main()  