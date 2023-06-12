class Student:
    ID = 1
    
    def __init__(self, name, score, ethnic_group, area) -> None:
        self.name, self.score, self.ethnic_group, self.area = name, score, ethnic_group, area
        
        self.id = 'TS{:02d}'.format(Student.ID)
        Student.ID += 1
        
    def calc_final_score(self):
        extras = [0, 1.5, 1, 0]
        extra = extras[int(self.area)]
        return self.score + extra if self.ethnic_group == 'Kinh' else self.score + extra + 1.5
    
    def format_name(self):
        return ' '.join(i.capitalize() for i in self.name.strip().split())
    
    def __str__(self) -> str:
        return f'{self.id} {self.format_name()} {self.calc_final_score():.1f} Do' if self.calc_final_score() >= 20.5 else f'{self.id} {self.format_name()} {self.calc_final_score():.1f} Truot'

def main():
    t = int(input())
    
    students = []
    while t > 0:
        name = input()
        score = float(input())
        ethnic_group = input()
        area = int(input())
        
        student = Student(name, score, ethnic_group, area)
        students.append(student)
        
        t -= 1
        
    students.sort(key=lambda student: (-student.calc_final_score(), student.id))
    
    for student in students:
        print(student)

if __name__ == '__main__':
    main()