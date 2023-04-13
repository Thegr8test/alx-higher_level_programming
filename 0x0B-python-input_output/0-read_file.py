#!/usr/bin/python3
"""defines a text file-reading funct"""


def read_file(filename=""):
    """displays contents of a UTF8 txt file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
