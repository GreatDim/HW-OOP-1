class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
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

    def get_average_grade(self):
        if not self.grades:
            return 0.0
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return round(total / count, 1) if count > 0 else 0.0

    def __str__(self):
        courses_str = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'нет'
        finished_str = ', '.join(self.finished_courses) if self.finished_courses else 'нет'
        avg_grade = self.get_average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg_grade}\n'
                f'Курсы в процессе изучения: {courses_str}\n'
                f'Завершенные курсы: {finished_str}')

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() < other.get_average_grade()
        return NotImplemented


    def __eq__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() == other.get_average_grade()
        return NotImplemented




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'




class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_lecture_grade(self):
        if not self.grades:
            return 0.0
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return round(total / count, 1) if count > 0 else 0.0

    def __str__(self):
        avg_grade = self.get_average_lecture_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {avg_grade}')

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_lecture_grade() < other.get_average_lecture_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_lecture_grade() == other.get_average_lecture_grade()
        return NotImplemented




class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'





def get_avg_student_grade_by_course(students, course):
    """
    Считает среднюю оценку за ДЗ по всем студентам на указанном курсе.
    :param students: список объектов Student
    :param course: название курса (str)
    :return: средняя оценка (float), округлённая до 1 знака после запятой
    """
    total_grades = []
    for student in students:
        if course in student.grades and student.grades[course]:
            total_grades.extend(student.grades[course])
    if not total_grades:
        return 0.0
    return round(sum(total_grades) / len(total_grades), 1)



def get_avg_lecturer_grade_by_course(lecturers, course):
    """
    Считает среднюю оценку за лекции по всем лекторам на указанном курсе.
    :param lecturers: список объектов Lecturer
    :param course: название курса (str)
    :return: средняя оценка (float), округлённая до 1 знака после запятой
    """
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades and lecturer.grades[course]:
            total_grades.extend(lecturer.grades[course])
    if not total_grades:
        return 0.0
    return round(sum(total_grades) / len(total_grades), 1)






student_1 = Student('Ольга', 'Алёхина', 'Ж')
student_2 = Student('Иван', 'Иванов', 'М')


lecturer_1 = Lecturer('Алексей', 'Петров')
lecturer_2 = Lecturer('Мария', 'Сидорова')


reviewer_1 = Reviewer('Дмитрий', 'Кузнецов')
reviewer_2 = Reviewer('Елена', 'Волкова')



student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']
student_2.courses_in_progress += ['Python', 'Java']


lecturer_1.courses_attached += ['Python']
lecturer_2.courses_attached += ['Java', 'Git']


reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2.courses_attached += ['Java']




reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Java', 7)
reviewer_2.rate_hw(student_2, 'Java', 9)


student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_2, 'Git', 8)
student_2.rate_lecture(lecturer_1, 'Python', 9)
student_2.rate_lecture(lecturer_2, 'Java', 7)



print('=== СТУДЕНТЫ ===')
print(student_1)
print('-' * 40)
print(student_2)

print('\n=== ЛЕКТОРЫ ===')
print(lecturer_1)
print('-' * 40)
print(lecturer_2)

print('\n=== РЕВИЗОРЫ ===')
print(reviewer_1)
print('-' * 40)
print(reviewer_2)



print('\n=== СРАВНЕНИЕ ===')
print(f'student_1 > student_2: {student_1 > student_2}')
print(f'lecturer_1 == lecturer_2: {lecturer_1 == lecturer_2}')



print('\n=== СРЕДНИЕ ОЦЕНКИ ПО КУРСАМ ===')


avg_student_python = get_avg_student_grade_by_course([student_1, student_2], 'Python')
print(f'Средняя оценка за ДЗ по курсу Python: {avg_student_python}')


avg_student_java = get_avg_student_grade_by_course([student_1, student_2], 'Java')
print(f'Средняя оценка за ДЗ по курсу Java: {avg_student_java}')


avg_lecturer_python = get_avg_lecturer_grade_by_course([lecturer_1, lecturer_2], 'Python')
print(f'Средняя оценка за лекции по курсу Python: {avg_lecturer_python}')


avg_lecturer_java = get_avg_lecturer_grade_by_course([lecturer_1, lecturer_2], 'Java')
print(f'Средняя оценка за лекции по курсу Java: {avg_lecturer_java}')


avg_student_git = get_avg_student_grade_by_course([student_1, student_2], 'Git')
print(f'Средняя оценка за ДЗ по курсу Git: {avg_student_git}')

avg_lecturer_git = get_avg_lecturer_grade_by_course([lecturer_1, lecturer_2], 'Git')
print(f'Средняя оценка за лекции по курсу Git: {avg_lecturer_git}')
