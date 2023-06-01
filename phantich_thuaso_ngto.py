def main():
    
    for test_num in range(1, int(input()) + 1):
        res = ['1']
        N = int(input())
        
        curr = 2
        count = 0
        
        while N > 1:
            while N % curr == 0:
                count += 1
                N /= curr
            
            res.append(f'{curr}^{count}') if count >= 1 else None
            curr += 1
            count = 0
        
        print(' * '.join(res))

if __name__ == '__main__':
    main()
