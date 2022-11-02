"""
Program: Person.py
Author: Alex Heinrichs
Date Created: 11/2/2022

Contains a person class with data for use in the Student class
"""


class Person:
    """Person class using class Address, Class Composition"""
    def __init__(self, lname, fname, addy=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def __str__(self):
        return str(self.last_name) + ", " + str(self.first_name) + '\n'\
              + self.address

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name) + '\n'\
              + self.address
