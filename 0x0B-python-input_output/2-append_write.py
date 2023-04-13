#!/usr/bin/python3
"""This module defines a file-appending function."""


def append_write(filename="", text=""):
    """adds a string to the end of the UTF8 txt file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
