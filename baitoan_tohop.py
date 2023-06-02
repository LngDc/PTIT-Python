from itertools import combinations

def solution():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    B = list(set(A))
    B.sort()

    combinations_list = list(combinations(B, K))
    for combination in combinations_list:
        print(*combination)

    

def main(func, t):
    for i in range(1, t + 1):
        func()

if __name__ == '__main__':
    main(solution, 1)