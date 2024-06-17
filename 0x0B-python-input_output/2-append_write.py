#!/usr/bin/python3
"""2-append_write module appends
a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a UTF8 text

    Args:
        filename (str): The file to append to.
        text (str): The text to append.


    Returns:
        int: The number of characters added.
    """
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
