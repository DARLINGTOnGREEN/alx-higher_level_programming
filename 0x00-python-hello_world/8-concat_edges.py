#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
language that combines remarkable power with very clear syntax"
str_value = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
print(str_value[str_value.find("object-oriented programming"):str_value.find("object-oriented programming") + len("object-oriented programming")], end="\n")

