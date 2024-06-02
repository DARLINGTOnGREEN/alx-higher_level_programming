#!/usr/bin/python3
"""Module that defines a class called Rectangle"""


class Rectangle:
    """Class named rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """that returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """return the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width = 0 or self.__height = 0:
            return ""
        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"
            rectangle += "\n"
        return rectangle

    def __rep__(self):
        return f"Rectangle({self.__width}, {self.__height})"
