#!/usr/bin/python3
"""Square based on 3-square"""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter method for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) for i in value) \
                or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.size ** 2

    def my_print(self):
        """print the square with '#' characters"""
        if self.size == 0:
            print()
            return

        for x in range(self.position[1]):
            print()

        for x in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
