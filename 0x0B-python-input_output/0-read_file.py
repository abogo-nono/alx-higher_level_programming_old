#!/usr/bin/python3
"""Read file content
"""

def read_file(filename=""):
    """this function is used to read an UTF-8 file and print his content in stdout

    Args:
        filename (str, optional): the name of the file t read. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")

# read_file('friends')