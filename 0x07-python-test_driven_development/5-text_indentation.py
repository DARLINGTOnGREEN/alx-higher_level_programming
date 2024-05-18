#!/usr/bin/python3
"""function that prints a text with 2 new \
        lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """check if the text is a string"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in [".", ",", "?", ":"]:

        text = text.replace(char, f"{char}\n\n")


    lines = text.split("\n")

    for index, line in enumerate(lines):

        if line:  # ignore empty lines

            print(line.strip())

            if index < len(lines) - 1:  # ignore the last line

                print()

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
