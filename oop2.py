class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_course = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
            return grade
        else:
            return 'Ошибка'




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []




class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}




class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)




# Создание объектов
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')


# Назначение курсов
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']


# Тестирование
print(isinstance(lecturer, Mentor))
print(isinstance(reviewer, Mentor))
print(lecturer.courses_attached)
print(reviewer.courses_attached)
print(student.rate_lecture(lecturer, 'Python', 7))
print(student.rate_lecture(lecturer, 'Java', 8))
print(student.rate_lecture(lecturer, 'C++', 8))
print(student.rate_lecture(reviewer, 'Python', 6))
print(lecturer.grades)