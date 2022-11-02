"""
Program: student.py
Author: Alex Heinrichs
Date Created: 11/2/2022

contains a class HourlyEmployee that is derived from Employee and
overrides a few methods within Employee
"""
from Topic4.employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, lname, fname, addy, phone_number, hpay, sdate):
        super().__init__(lname, fname, addy, phone_number)
        self.hourly_pay = hpay
        self.start_date = sdate

    def give_raise(self, hpay):
        self.hourly_pay = hpay

    def display(self):
        return super().display() + '\nHourly pay: ' + str(self.hourly_pay) \
               + '\nStart date: ' + self.start_date


if __name__ == '__main__':
    hemp = HourlyEmployee('Heinrichs', 'Alex', '123 Lane', '6416919494', 10.00, '11/2/2022')
    print(hemp.display())
    hemp.give_raise(12.00)
    print(hemp.display())
