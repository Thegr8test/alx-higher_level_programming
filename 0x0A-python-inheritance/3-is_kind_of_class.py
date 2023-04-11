#!/usr/bin/python3
"""checks if object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """returns true if object is an instance of a class
    or class it inherits from
    """
    return (isinstance(obj, a_class))
