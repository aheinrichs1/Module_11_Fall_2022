"""
Program: employee.py
Author: Alex Heinrichs
Date created: 11/2/2022

Contains a class called employee which demonstrates encapsulation
"""
from Topic4.person import Person


class Employee(Person):
    """Employee Class"""

    # Constructor
    def __init__(self, lname, fname, addy, p_number, s_date, sal):
        super().__init__(lname, fname, addy, p_number)
        self._start_date = s_date
        self._salary = sal

    def change_salary(self, sal):
        self._salary = sal

    def display(self):
        return super().display() + '\nStart date: ' + self._start_date \
               + '\nSalary: ' + str(self._salary)

    def __str__(self):
        return '\nStart date: ' + self._start_date \
               + '\nSalary: ' + str(self._salary)

    def __repr__(self):
        return '\nStart date: ' + self._start_date \
               + '\nSalary: ' + str(self._salary)


if __name__ == "__main__":
    emp = Employee("Heinrichs", "Alex", "317 East St.\nAmes, Iowa",
                   "641-691-9494", "11/2/2022", "6416919494")
    print(emp.display())
    print(emp)
    del emp
