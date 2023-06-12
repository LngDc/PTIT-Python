class Line:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def main():
    t = int(input()) + 1
    
    for i in range(1, t):
        line_count = int(input())
        lines = []
        
        for i in range(line_count):
            x, y = map(int, input().split())
            line = Line(x, y)
            lines.append(line)
            
        lines.sort(key=lambda line: line.y)
        
        count = 1
        curr = lines[0].y
        
        for j in range(1, line_count):
            if lines[j].x >= curr:
                count += 1
                curr = lines[j].y
        
        print(count)
        

if __name__ == '__main__':
    main()