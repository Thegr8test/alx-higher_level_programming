#!/usr/bin/python3
"""inherits from the list class"""


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        """displays a sorted list"""
        print(sorted(self))
