def check(s1, s2):
    return ''.join(sorted(s1)) == ''.join(sorted(s2))

def main():
    t = int(input())
    for test in range(1, t + 1):
        s1 = input()
        s2 = input()

        print(f'Test {test}: YES' if check(s1, s2) else f'Test {test}: NO')

if __name__ == '__main__':
    main()