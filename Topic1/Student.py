"""
Program: Student.py
Author: Alex Heinrichs
Date Created: 11/2/2022

Contains a student class that has a data member of the
type of a class you defined (Person)
"""
from Topic1.Person import Person


class Student:
    """Student class"""
    def __init__(self, p, major, start, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        start_date_characters = set('1234567890/')
        gpa_characters = set("1234567890.")
        if not name_characters.issuperset(major):
            raise ValueError
        if not start_date_characters.issuperset(start):
            raise ValueError
        if not isinstance(gpa, float) or (gpa < 0.0) or (gpa > 4.0):
            raise ValueError
        self.person = p
        self.major = major
        self.start_date = start
        self.gpa = gpa

    def __str__(self):
        return self.person + ", " + " has major " + self.major + " with gpa: " + str(self.gpa) \
               + "and started on " + self.start_date

    def change_major(self, maj):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-! ")
        if not name_characters.issuperset(maj):
            raise ValueError
        self.major = maj

    def update_gpa(self, gpa):
        gpa_characters = set("1234567890.")
        if not isinstance(gpa, float) or (gpa < 0.0) or (gpa > 4.0):
            raise ValueError
        self.gpa = gpa

    def display(self):
        return str(self.person) + ", has major " + self.major + " with gpa: " + str(self.gpa) \
               + " and started on " + self.start_date


if __name__ == '__main__':
    person1 = Person('Heinrichs', 'Alex', '123 Lane')
    student1 = Student(person1, 'CIS', '01/01/2022', 4.0)
    print(student1.display())
    student1.change_major('Being Awesome!')
    student1.update_gpa(3.0)
    print(student1.display())
    del student1

