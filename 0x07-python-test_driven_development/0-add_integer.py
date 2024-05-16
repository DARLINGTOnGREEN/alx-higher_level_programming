#!/usr/bin/python3
"""function to add two integer or float"""


def add_integer(a, b=98):
    """Adds two integer or floats together
    and returns the result
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
