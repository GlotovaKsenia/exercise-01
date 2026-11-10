class Exam:
    weight = 1
    def __init__(self, grade):
        self.grade = grade
    def weighted_grade(self):
        return self.grade * self.weight
    
class WrittenExam(Exam):
    weight = 2
    
class ProjectWork(Exam):
    weight = 1

class Student:
    def __init__(self, name, exams: list[Exam]| None = None):
        self.n = name
        self.exams = exams if exams else []

    def add_exam(self, exam: Exam):
        self.exams.append(exam)

    def average(self):
        total_grades = sum(exam.weighted_grade() for exam in self.exams)
        total_weight = sum(exam.weight for exam in self.exams)
        return round(total_grades / total_weight, 2)

    def __str__(self):
        return f"{self.n}: {self.average()}"

class Course:
    def __init__(self, name, students: list[Student] | None = None):
        self.n = name
        self.students = students if students else []

    def add_student(self, student: Student):
        self.students.append(student)

    def average(self):
        total = sum(student.average() for student in self.students)
        return round(total / len(self.students), 2)
    
    def best(self):
        best = min(self.students, key=lambda student: student.average())
        return best.n, best.average()

if __name__=="__main__":
    course = Course("Test Kurs", )

    data: list[tuple[str, type[Exam], float]] = [
        ("Lena", WrittenExam, 1.7),
        ("Jonas", ProjectWork, 2.3),
        ("Alex", WrittenExam, 3.0),
        ("Mika", ProjectWork, 4.3),
        ("Deniz", WrittenExam, 1.3),
        ("Sam", ProjectWork, 2.7),
    ]

    for name, exam, grade in data:
        student = Student(name)
        student.add_exam(exam(grade))
        course.add_student(student)

    print("Kursdurchschnitt: ", course.average())
    print("Best: ", course.best())