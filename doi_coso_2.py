from math import log2

def main():
    BASE_2 = {
        '0': '0',
        '1': '1',
    }
    
    BASE_4 = {
        '00': '0',
        '01': '1',
        '10': '2',
        '11': '3'
    }
    
    BASE_8 = {
        '000': '0',
        '001': '1',
        '010': '2',
        '011': '3',
        '100': '4',
        '101': '5',
        '110': '6',
        '111': '7'
    }
    
    BASE_16 = {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'A',
        '1011': 'B',
        '1100': 'C',
        '1101': 'D',
        '1110': 'E',
        '1111': 'F'
    }
    
    t = int(input())
    while t > 0:
        BASE = int(input())
        CAP = int(log2(BASE))
        
        num = input()
        while len(num) % CAP:
            num = '0' + num
        # num = num[::-1]

        splits = [num[i:i + CAP] for i in range(0, len(num), CAP)]
        
        find_base = f'BASE_{BASE}'
        selected_dict = locals()[find_base]
        res = [selected_dict[x] for x in splits]
        
        print(''.join(res))
        
        t -= 1
        

if __name__ == '__main__':
    main()