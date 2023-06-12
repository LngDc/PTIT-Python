res = []

def Try(N, i, sum, nums):
    if sum > N: return
    if sum == N: 
        res.append(nums[:])
        return
    for j in range(i, 0, -1):
        Try(N, j, sum + j, nums + [j])
    
        
def main():
    t = int(input()) + 1
    
    for i in range(1, t):
        N = int(input())
        
        Try(N, N, 0, [])
        
        print(len(res))
        for comb in res:
            print('(', end='')
            print(*comb, sep=' ', end='')
            print(') ', end='')
        print()
        
        res.clear()
    
    

if __name__ == '__main__':
    main()