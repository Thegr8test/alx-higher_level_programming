#!/usr/bin/python3
"""defines a class called MyInt that inherits from int"""


class MyInt(int):
    """class that inverts the int operators"""

    def __eq__(self, value):
        """Override operator behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override operator behavior"""
        return self.real == value
