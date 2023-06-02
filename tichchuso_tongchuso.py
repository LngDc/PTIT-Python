from functools import reduce

def solution():
    number = input()
    even_digits = [int(i) for i in number[::2] if int(i) != 0]
    odd_digits = [int(i) for i in number[1::2]]
    
    product_even = reduce(lambda x, y: x * y, even_digits)
    sum_odd = sum(odd_digits)
    
    print(f'{product_even} {sum_odd}')

def main(func, t):
    for i in range(1, t + 1):
        func()

if __name__ == '__main__':
    main(solution, int(input()))