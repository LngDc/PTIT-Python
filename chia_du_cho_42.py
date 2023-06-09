def main():
    A = []
    
    while len(A) != 10:
        A.extend(list(map(int, input().split())))
        
    B = set()
    
    for x in A:
        B.add(x % 42)
    
    print(len(B))

if __name__ == '__main__':
    main()