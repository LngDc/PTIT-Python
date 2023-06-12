from datetime import datetime

class Subject:
    def __init__(self, subject_id, subject_name) -> None:
        self.subject_id = subject_id
        self.subject_name = subject_name

class Exam:
    ID = 1
    
    def __init__(self, exam_info) -> None:
        self.exam_info = exam_info.split()
        self.subject_id, self.date, self.time, self.group = self.exam_info
        
        self.id = f'T{Exam.ID:03d}'
        Exam.ID += 1
        
        self.date_time = datetime.strptime(self.date, '%d/%m/%Y')
        self.time_time = datetime.strptime(self.time, '%H:%M')
        
    def set_subject_name(self, subject_name):
        self.subject_name = subject_name
        
    def __str__(self) -> str:
        return f'{self.id} {self.subject_id} {self.subject_name} {self.date} {self.time} {self.group}'

def main():
    subject_count, exam_count = map(int, input().split())
    
    subjects = []
    for i in range(subject_count):
        subject_id, subject_name = input(), input()
        subject = Subject(subject_id, subject_name)
        subjects.append(subject)
    
    exams = []
    for j in range(exam_count):
        exam_info = input()
        exam = Exam(exam_info)
        exam_object = next(filter(lambda x: x.subject_id == exam.subject_id, subjects))
        exam.set_subject_name(exam_object.subject_name)
        exams.append(exam)
        
    exams.sort(key = lambda x: (x.date_time, x.time_time, x.id))
    
    for exam in exams:
        print(exam)
        
    
        
if __name__ == '__main__':
    main()