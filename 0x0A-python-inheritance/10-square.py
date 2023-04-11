#!/usr/bin/python3
"""Defines a Rectangle subclass Square....duh!"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Reps a square"""

    def __init__(self, size):
        """Initialize new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
