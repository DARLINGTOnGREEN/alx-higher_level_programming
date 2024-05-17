#!/usr/bin/python3
"""Function at print a Square using #."""


def print_square(size):
    """print a Square using #"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("x" * size)
