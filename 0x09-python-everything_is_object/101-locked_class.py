#!/usr/bin/python3
"""it defines a locked class"""


class LockedClass:
    """
    strictly allows instatiation of an attribute called first_name
    """

    __slots__ = ["first_name"]
