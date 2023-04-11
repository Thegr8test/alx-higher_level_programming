#!/usr/bin/python3
"""checks object if is an instance of a class that
inherited from the specified class
"""


def inherits_from(obj, a_class):
    """Returns true if object is an instance of a class that inherited
    from the specified class, else False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
