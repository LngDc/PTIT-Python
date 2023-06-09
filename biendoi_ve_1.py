def main():
    while 1:
        N = int(input())
        if N == 0: break
        
        steps = []
        steps.append(N)
        
        while N != 1:
            if N % 2 == 0:
                N /= 2
            else:
                N = N * 3 + 1
            steps.append(N)
            
        print(len(steps))
        

if __name__ == '__main__':
    main()
    