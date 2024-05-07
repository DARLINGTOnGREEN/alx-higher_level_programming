#!/usr/bin/python3
"""Square based on 3-square"""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initializes the data."""
        self.size = size

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.size ** 2

    def my_print(self):
        """print the square with '#' characters"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
