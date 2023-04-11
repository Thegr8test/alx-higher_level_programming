#!/usr/bin/python3
"""defines a function that sums attributes to objects"""


def add_attribute(obj, att, value):
    """Adds attribute to an object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
