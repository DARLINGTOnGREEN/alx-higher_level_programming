#!/usr/bin/python3
"""Module 4-from_json_string.
Returns an object
represented by a JSON string.
"""


import json


def from_json_string(my_str):
    """from_json_string function
    Args:
        - my_str: JSON string representation
    Returns: corresponding object
    """

    return json.loads(my_str)
