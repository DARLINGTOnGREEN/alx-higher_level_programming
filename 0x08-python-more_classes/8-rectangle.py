#!/usr/bin/python3
"""
This module defines a Rectangle class that allows you to
create rectangles with specified width and height.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with optional width and height.

        Parameters:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Return a string representation of the rectangle using the print_symbol.

        Returns:
        str: String representation of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        size = str(self.print_symbol) * self.__width
        rect = [size] * self.__height
        return "\n".join(rect)

    def __repr__(self):
        """
        Return a string representation of the Rectangle instance.

        Returns:
        str: A string representation of the rectangle.
        """
        return "{:s}({:d}, {:d})".format(type(self).__name__,
                                         self.__width, self.__height)

    def __del__(self):
        """
        Print a message when the Rectangle instance is deleted
        and decrease the instance count.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
        int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with validation.

        Parameters:
        value (int): The width to set.

        Raises:
        TypeError: If the width is not an integer.
        ValueError: If the width is less than 0.
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

        Returns:
        int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation.

        Parameters:
        value (int): The height to set.

        Raises:
        TypeError: If the height is not an integer.
        ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare the areas of two rectangles and return the bigger or equal one.

        Parameters:
        rect_1 (Rectangle): The first rectangle to compare.
        rect_2 (Rectangle): The second rectangle to compare.

        Returns:
        Rectangle: The rectangle with the larger or equal area.

        Raises:
        TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
