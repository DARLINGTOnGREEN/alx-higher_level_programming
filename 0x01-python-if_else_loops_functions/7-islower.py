#!/usr/bin/python3
def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

# Test the function
print(islower('a'))  # Output: True
print(islower('B'))  # Output: False
print(islower('5'))  # Output: False

