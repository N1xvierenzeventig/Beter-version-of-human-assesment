from Code import Student
import random

Nikita = Student("Nikita", 16, 8.5, "Handsome", True, False, True, True)
Timur = Student("Timur", 16, 8.3, "Very good", True, True, True, True)
Dima = Student("Dima", 16, 7.3, "Ok", True, True, False, True)
Mark = Student("Mark", 16, 8.2, "Very good", True, True, True, True)

Information = []
q = int(input("Input amount of students: "))
def generate_random_student():
    for i in range(q):
        name = "Student " + str(random.randint(1, 100))
        av_mark = random.randint(5,10)
        appearance = random.choice(["Handsome", "Very good", "Ok", "Poor"])
        doing_sport = random.choice([True, False])
        is_kind = random.choice([True, False])
        intelligent= random.choice([True, False])
        nice_clothes = random.choice([True, False])
        student = Student(name, 16, av_mark, appearance, doing_sport, is_kind, intelligent, nice_clothes)
        Information.append(student)

def assessment(Information):
    List1 = []
    for Student in Information:
        Student_Mark = 0
        if Student.av_mark > 8:
            Student_Mark += 2
        if Student.appearance == "Handsome":
            Student_Mark += 3
        elif Student.appearance == "Very good":
            Student_Mark += 2
        elif Student.appearance == "Ok":
            Student_Mark += 1
        if Student.doing_sport is True:
            Student_Mark += 1
        if Student.is_kind is True:
            Student_Mark += 1
        if Student.intelligent is True:
            Student_Mark += 2
        if Student.nice_clothes is True:
            Student_Mark += 1
        List1.append([Student.name, Student_Mark])
    List1.sort(key=lambda x: x[1], reverse=True)
    print(List1[:q])

generate_random_student()
assessment(Information)


