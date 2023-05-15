class ThiSinh:
    def __init__(self, name, dob, x1, x2, x3) -> None:
        self.name = name
        self.dob = dob
        self.res = x1 + x2 + x3
        
    def __str__(self) -> str:
        return f'{self.name} {self.dob} {self.res:.1f}'
        

def main():
    name = input()
    dob = input()
    x1 = float(input())
    x2 = float(input())
    x3 = float(input())
    thisinh = ThiSinh(name, dob, x1, x2, x3)
    print(thisinh)

if __name__ == '__main__':
    main()
