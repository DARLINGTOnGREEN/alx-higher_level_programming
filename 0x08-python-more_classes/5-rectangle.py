#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with optional width and height.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        Return a string representation of the rectangle with the character #.
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        size = "#" * self.__width
        rect = []
        for _ in range(self.__height):
            rect.append(size)
        return "\n".join(rect)

    def __repr__(self):
        """
        Return a string representation of the Rectangle instance.
        """
        return "{:s}({:d}, {:d})".format(type(self).__name__,
                                         self.__width, self.__height)

    def __del__(self):
        """
        Print a message when the Rectangle instance is deleted.
        """
        print("Bye rectangle...")

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with validation.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
