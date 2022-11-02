"""

Program: employee.py
Author: Alex Heinrichs
Date created: 11/2/2022

Contains a class called employee which demonstrates encapsulation
"""
import datetime


class Employee:
    """Employee Class"""

    # Constructor
    def __init__(self, lname, fname, addy, phone_number):
        self._last_name = lname
        self._first_name = fname
        self._address = addy
        self._phone = phone_number

    def display(self):
        return str(self._first_name) + " " + str(self._last_name) + "\n" \
               + self._address

    def __str__(self):
        return "First name: " + self._first_name \
                + "\nLast name: " + self._last_name \
                + "\nAddress: " + self._address \
                + "\nPhone number: " + self._phone

    def __repr__(self):
        return "First name: " + self._first_name \
                + "\nLast name: " + self._last_name \
                + "\nAddress: " + self._address \
                + "\nPhone number: " + self._phone


if __name__ == "__main__":
    emp = Employee("Heinrichs", "Alex", "317 East St.\nAmes, Iowa",
                   "641-691-9494")
    print(emp.display())
    print(emp)
    del emp
