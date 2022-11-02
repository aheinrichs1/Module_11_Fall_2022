"""
Program: student.py
Author: Alex Heinrichs
Date Created: 11/2/2022

Contains a class Student that inherits from class Person and
run basic code on it to test its functionality
"""
from Topic2.person import Person


class Student(Person):
    """Student class"""

    def __init__(self, sid, lname, fname, major='Computer Science', gpa=0.0):
        super().__init__(lname, fname)
        self._student_id = sid
        self._major = major
        self._gpa = gpa

    def __str__(self):
        return super().display() + '(' + str(self._student_id) + ') ' + self._major + ' gpa: ' + str(self._gpa)

    def display(self):
        return super().display() + '(' + str(self._student_id) + ') ' + self._major + ' gpa: ' + str(self._gpa)


# Driver
if __name__ == '__main__':
    my_student = Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    print(my_student.display())
    del my_student
