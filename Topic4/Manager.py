"""
Program: student.py
Author: Alex Heinrichs
Date Created: 11/2/2022

Contains a class named Manager that inherits both from Person and Employee
"""
from Topic4.employee import Employee


class Manager(Employee):
    def __init__(self, lname, fname, addy, p_number, s_date, sal, dpt, d_reports=[]):
        super().__init__(lname, fname, addy, p_number, s_date, sal)
        self._department = dpt
        self._direct_reports = d_reports

    def add_to_reports(self, emp):
        self._direct_reports.append(emp)

    def display(self):
        reports_string = ''
        for report in self._direct_reports:
            reports_string += report.display() + '\n'
        if reports_string == '':
            return super().display() + '\nDepartment: ' \
                   + self._department
        else:
            return super().display() + '\nDepartment: ' \
                   + self._department + '\nDirect Reports:\n' + reports_string


if __name__ == '__main__':
    man1 = Manager('Heinrichs', 'Alex', '123 Lane', '6416919494',
                   '11/2/2022', 40000, 'Computer')
    print(man1.display())
    print('\n\n')
    emp1 = Employee('Smith', 'John', '234 Avenue', '5155551234', '11/2/2022', 40000)
    emp2 = Employee('Joe', 'Axle', '234 Avenue', '5155551234', '12/12/1212', 50000)
    emp3 = Employee('Axel', 'Rose', 'Paris', '12345678', '11/2/2022', 35000)
    man1.add_to_reports(emp1)
    man1.add_to_reports(emp2)
    man1.add_to_reports(emp3)
    print(man1.display())
    print('\n\n')
    man1.change_salary(42000)
    print(man1.display())
