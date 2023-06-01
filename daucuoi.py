def main():
    for i in range(int(input())):
        number = input()
        
        print('YES' if number[:2] == number[-2:] else 'NO')
        
        

if __name__ == '__main__':
    main()
