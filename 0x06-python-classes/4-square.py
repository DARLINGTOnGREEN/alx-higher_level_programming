#!/usr/bin/python3
"""Defines on Square based on 3-square"""


class Square:

    """A class that defines a square"""

    def __init_(self, size=0):
        """Initialize the Square instance"""

        self.size = size

    def area(self):
        """Return the area of the square"""
        return self.size ** 2

    @property
    def size(self):
        """Retrives the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
