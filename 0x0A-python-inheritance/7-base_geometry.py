#!/usr/bin/python3

"""Defs geometry class BaseGeometry."""


class BaseGeometry:
    """Reps basegeometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): name of the parameter.
            value (int): parameter to validate.
        Raises:
            TypeError: If value !=int .
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
