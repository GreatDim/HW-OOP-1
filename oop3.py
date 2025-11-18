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

    def __le__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() <= other.get_average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() == other.get_average_grade()
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() > other.get_average_grade()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() >= other.get_average_grade()
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

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_lecture_grade() <= other.get_average_lecture_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_lecture_grade() == other.get_average_lecture_grade()
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_lecture_grade() > other.get_average_lecture_grade()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_lecture_grade() >= other.get_average_lecture_grade()
        return NotImplemented



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)






lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Пётр', 'Петров')
reviewer = Reviewer('Алексей', 'Сидоров')
student1 = Student('Ольга', 'Алёхина', 'Ж')
student2 = Student('Иван', 'Иванов', 'М')


student1.courses_in_progress += ['Python', 'Java']
student1.finished_courses += ['Введение в программирование']
student1.grades['Python'] = [9, 8, 10]
student1.grades['Java'] = [7, 9]

student2.courses_in_progress += ['Python']
student2.grades['Python'] = [10, 10, 10]

lecturer1.courses_attached += ['Python']
lecturer1.grades['Python'] = [8, 9, 10]

lecturer2.courses_attached += ['Java']
lecturer2.grades['Java'] = [7, 7, 8]

print(reviewer)
print()
print(lecturer1)
print()
print(lecturer2)
print()
print(student1)
print()
print(student2)

print("lecturer1 < lecturer2:", lecturer1 < lecturer2)
print("student1 > student2:", student1 > student2)
