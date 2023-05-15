import math

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier

class Student:
    ID = 1
    def __init__(self, name, score_list) -> None:
        self.id = f'HS{Student.ID:02d}'
        Student.ID += 1
        self.name = name
        
        scores = [score for score in score_list] 
        self.avg = (sum(scores)+ float(score_list[0]) + float(score_list[1])) / (len(scores) + 2)
        self.avg = round_half_up(self.avg, 1)
        
    def get_result(self) -> str:
        if self.avg < 5:
            return 'YEU'
        elif self.avg < 7:
            return 'TB'
        elif self.avg < 8:
            return 'KHA'
        elif self.avg < 9:
            return 'GIOI'
        else:
            return 'XUAT SAC'
    
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.avg} {self.get_result()}'

    
def main():
    student_list = []
    
    n = int(input())
    while n > 0:
        name = input()
        score_list = [float(score) for score in input().split()]
        student = Student(name, score_list)
        student_list.append(student)
        n -= 1
        
    student_list = sorted(student_list, key=lambda student: (-student.avg, student.id))
    
    for student in student_list:
        print(student)

if __name__ == '__main__':
    main()
