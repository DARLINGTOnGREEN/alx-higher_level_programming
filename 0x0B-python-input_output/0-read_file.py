#!/usr/bin/python3
"""0-read_file.py module reads
a file and prints"""


def read_file(filename=""):
    """ function that reads from a filename and prints
    its contents to stdout.

    args:
    filename: name of the file
    """
    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
