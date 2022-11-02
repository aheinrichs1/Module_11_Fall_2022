"""
Program: student.py
Author: Alex Heinrichs
Date Created: 11/2/2022

contains a class SalariedEmployee that is derived from Employee and
overrides a few methods within Employee
"""
from Topic3.employee import Employee


class SalariedEmployee(Employee):
    def __init__(self, lname, fname, addy, phone_number, sdate, salary):
        super().__init__(lname, fname, addy, phone_number)
        self.start_date = sdate
        self.salary = salary

    def give_raise(self, newsal):
        self.salary = newsal

    def display(self):
        return super().display() + '\nStart date: ' + self.start_date \
               + '\nSalary: ' + str(self.salary)


if __name__ == '__main__':
    semp = SalariedEmployee('Heinrichs', 'Alex', '123 Lane', '6416919494', '11/2/2022', 40000)
    print(semp.display())
    semp.give_raise(45000)
    print(semp.display())
