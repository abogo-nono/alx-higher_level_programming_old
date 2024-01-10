#!/usr/bin/python3
"""write in file
"""


def write_file(filename="", text=""):
    """Write a content in a file

    Args:
        filename (str, optional): file name. Defaults to "".
        text (str, optional): content to write. Defaults to "".
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    return len(text)
