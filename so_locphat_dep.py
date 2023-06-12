def check(s):
    if s[0] != '6':
        return False
    if s.count('888'):
        return False
    if any(digit != '6' and digit != '8' for digit in s):
        return False
    return True

def main():
    print('YES' if check(input()) else 'NO')

if __name__ == '__main__':
    main()