#!/usr/bin/python3
"""defines a file-writing funct."""


def write_file(filename="", text=""):
    """Writes the string to a UTF8 txt file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
