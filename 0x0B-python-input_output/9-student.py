#!/usr/bin/python3
"""Module 9-student.py
defines a class Student.
"""


class Student:
    """A class called Student.
    defines the student
    -first_name
    -last_name
    -age
    """

    def _init_(self, first_name, last_name, age):
        """Initialize the student with first name, last name, and age."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrives a dictionary representation
        of student instance
        Returns: the dictionary representation of the instance
        """

        return self.__dict__
