def main():
    a, K, N = map(int, input().split())

    curr = 0
    b = int()
    res = []
    
    while b <= N - a:
        curr += K
        b = curr - a
        
        if b > N - a: break
        if b <= 0: continue
        
        res.append(b)
        
    if len(res) == 0:
        print(-1)
    else:
        print(*res)
        
if __name__ == '__main__':
    main()
