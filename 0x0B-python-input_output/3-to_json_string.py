#!/usr/bin/python3
"""Module 3-to_json_string.py
Retunr the JSON representation of an object
"""


import json


def to_json_string(my_obj):

    """to_json_string function
    Args:
    - my_obj: string to represent
    Returns: JSON representation
    """

    return json.dumps(my_obj)
