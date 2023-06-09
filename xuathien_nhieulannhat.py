def main():
    t = int(input())
    while t > 0:
        N = int(input())
        
        A = list(map(int, input().split()))
        if len(A) == 1:
            print(A[0])
        else:
            pairs, res_key, res_value = {}, A[0], 1
            
            for i in A:
                if i in pairs:
                    pairs[i] += 1
                    if pairs[i] > res_value:
                        res_key = i
                        res_value = pairs[i]
                else:
                    pairs[i] = 1
        
            if res_value * 2 > N:
                print(res_key)
            else:
                print('NO')     
            
        t -= 1  
        
                    

if __name__ == '__main__':
    main()