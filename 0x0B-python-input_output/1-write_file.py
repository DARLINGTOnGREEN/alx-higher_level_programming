#!/usr/bin/python3
"""Module 1-write_file.
Writes in a text file.
"""


def write_file(filename="", text=""):
    """Function that writes text in filename.
    Args:
        - filename: name of the file
        - text: write in the file
    Returns: number of characters written
    """

    with open(filename, 'w+') as f:
        return f.write(text)
