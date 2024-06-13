#!/usr/bin/python3
"""Module that defines a function"""


def inherits_from(obj, a_class):
    """function inherits_from
    returns true if obj is a class
    else false
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
