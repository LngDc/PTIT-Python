def main():
    t = int(input())
    while t > 0:
        N = int(input())
        
        loop_count = 0
        
        while loop_count < 1001 and N % 7 != 0:
            N += int(str(N)[::-1])
              
            loop_count += 1
        
        if loop_count == 1001: print(-1)
        else: print(N)
        
        t -= 1
    
        
        

if __name__ == '__main__':
    main()
