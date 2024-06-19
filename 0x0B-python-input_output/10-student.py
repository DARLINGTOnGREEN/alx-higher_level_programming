#!/usr/bin/python3
"""Module 10-student.py.
Creates a class called student.
"""


class Student:
    """Defines the class Student.
    Public attributes:
    -first_name
    -last_name
    -age
    Public method to_json().
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation
        of a Student instance.
        Args:
            - attrs: list of attributes
        Returns: the dict representation of the instance.
        """

        my_dict = dict()
        if type(attrs) is list and all(type(i) is str for i in attrs):
            for i in attrs:
                if i in self.__dict__:
                    my_dict.update({i: self.__dict__[i]})
            return my_dict
        return self.__dict__.copy()
