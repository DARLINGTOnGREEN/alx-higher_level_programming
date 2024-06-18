#!/usr/bin/python3
"""Module 5-save_to_json_file.
Writes an Object to a text file,
using a JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file function
    Args:
        - my_obj: object to write
        - filename: file to write into
    """

    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
