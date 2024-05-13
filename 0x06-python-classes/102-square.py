#!/usr/bin/pyhton3
"""define a class called square"""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize the Square."""
        self.size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Define equality comparator."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """Define inequality comparator."""
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        return not result

    def __gt__(self, other):
        """Define greater than comparator."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Define greater than or equal to comparator."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """Define less than comparator."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Define less than or equal to comparator."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

