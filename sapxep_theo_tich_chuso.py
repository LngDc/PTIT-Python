from functools import reduce

def calc_prod(n):
    digits = [int(i) for i in n]
    return reduce(lambda x, y: x * y, digits)

def main():
    t = int(input())
    while t > 0:
    
        N = int(input())
        A = input().split()
        
        pairs = {}
        for i in A:
            pairs[i] = calc_prod(i)
            
        A = sorted(A, key=lambda x: (pairs[x], int(x)))
        print(*A)
        
        t -= 1

    
    
    

if __name__ == '__main__':
    main()  