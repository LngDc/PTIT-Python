def main():
    for test_num in range(1, int(input()) + 1):
        number = [int(i) for i in input()]
        length = len(number)
        
        for index in range(length - 1, 0, -1):
            if number[index] >= 5:
                number[index - 1] = number[index - 1] + 1
            
            number[index] = 0
        
        # if number[0] == 10:
        #     number[0] = 0
        #     number = [1] + number

        print(''.join(str(i) for i in number))
            

if __name__ == '__main__':
    main()
