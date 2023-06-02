from itertools import permutations

def solution():
    string = input()
    
    permutations_list = list(permutations(string))
    for permutation in permutations_list:
        curr_perm = ''.join(permutation)
        print(curr_perm)

    

def main(func, t):
    for i in range(1, t + 1):
        func()

if __name__ == '__main__':
    main(solution, 1)