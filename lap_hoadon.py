class Bill:
    ID = 1
    
    def __init__(self, name, prev_stat, new_stat) -> None:
        self.id = f'KH{Bill.ID:02d}'
        Bill.ID += 1
        self.name = name
        self.consume = new_stat - prev_stat    
        
    def calc(self):
        
        if self.consume <= 50:
            return self.consume * 100 + self.consume * 100 * 2 / 100
        elif self.consume <= 100:
            price = 50 * 100 + (self.consume - 50) * 150
            return price + price * 3 / 100
        else:
            price = 50 * 100 + 50 * 150 + (self.consume - 100) * 200
            return price + price * 5 / 100
            
        
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.calc():.0f}'
        
    
def main():
    n = int(input())
    bill_list = []
    
    while n > 0:
        name = input()
        prev_stat = int(input())
        new_stat = int(input())
        bill = Bill(name, prev_stat, new_stat)
        bill_list.append(bill)
        
        n -= 1
        
    bill_list = sorted(bill_list, key=lambda bill: -bill.calc())
    
    for bill in bill_list:
        print(bill)
        

if __name__ == '__main__':
    main()
