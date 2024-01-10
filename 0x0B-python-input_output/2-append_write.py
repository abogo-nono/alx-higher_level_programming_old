#!/usr/bin/python3
"""append a file
"""


def append_write(filename="", text=""):
    """append the content of a file

    Args:
        filename (str, optional): file name. Defaults to "".
        text (str, optional): content to write. Defaults to "".
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
