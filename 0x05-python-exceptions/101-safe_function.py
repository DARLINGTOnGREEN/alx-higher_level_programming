#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except Exception:
        print("Exceptions: {}".format(sys.exe_ifo()[1]), file=sys.stderr)
        return (None)
