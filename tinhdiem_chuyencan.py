class Student:
    def __init__(self, id, name, class_id) -> None:
        self.id = id
        self.name = name
        self.class_id = class_id
        self.score = 10
        self.condition = 'KDDK'
        
    def calc_score(self, report_card):
        self.score = 10 - report_card.count('m') - report_card.count('v') * 2
        if self.score < 0:
            self.score = 0
    
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.class_id} {self.score}' if self.score != 0 else f'{self.id} {self.name} {self.class_id} {self.score} {self.condition}'

    
def main():
    n = int(input())
    n_0 = n
    student_list = []
    
    while n > 0:
        id = input()
        name = input()
        class_id = input()
        student = Student(id, name, class_id)
        student_list.append(student)
        
        n -= 1
        
    while n_0 > 0:  
        student_id, report_card = input().split()
        student_object = next(filter(lambda x: x.id == student_id, student_list))
        student_object.calc_score(report_card)
        
        n_0 -= 1
    
    for student in student_list:
        print(student)

if __name__ == '__main__':
    main()
