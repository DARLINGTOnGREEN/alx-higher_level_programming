#!/usr/bin/pyhton3
"""function that add two interger for float"""


def add_integer(a, b=98):
    """Adds two integer or floats together
    and returns the result
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a and b must be integers or floats")

    if not isinstance(b, (int, float)):
        raise TypeError("a and b must be integers or floats")

    a = int(a)
    b = int(b)

    return a + b
