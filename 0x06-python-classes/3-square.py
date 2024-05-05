#!/usr/bin/python3
"""Area of square"""


class Square:
    """Define an area of a square"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be aj integer")
        elif type(size) < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

    def area(self):
        """calculate and return the area of the square."""
        return self.__size ** 2
