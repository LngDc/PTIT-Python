def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    i = 1
    while i < len(A):
        if (A[i - 1] + A[i]) % 2 == 0:
            A.pop(i - 1)
            A.pop(i - 1)
            
            if i > 1:
                i -= 1
        else:
            i += 1
    
    print(len(A))        
        

if __name__ == '__main__':
    main()