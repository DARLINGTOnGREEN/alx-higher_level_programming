#!/usr/bin/python3
"""A module that defines a class called MagicClass"""


class MagicClass:
    """A class that performs magic"""

    def __init__(self, radius=0):
        """Initialize the MagicClass with a radius"""
        self.radius = radius

    @property
    def radius(self):
        """Getter method for the radius"""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Setter method for the radius"""
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")
        if value < 0:
            raise ValueError("radius must be >= 0")
        self.__radius = value

    def area(self):
        """Calculate and return the area of the circle"""
        return self.__radius ** 2 * 3.14159

    def circumference(self):
        """Calculate and return the circumference of the circle"""
        return 2 * 3.14159 * self.__radius


if __name__ == "__main__":
    mc = MagicClass(10)
    print("{:.2f}".format(mc.area()))  # Correct output: 314.16
    print("{:.2f}".format(mc.circumference()))  # Correct output: 62.83
