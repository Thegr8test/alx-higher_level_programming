#!/usr/bin/python3
"""module that defines a Python class-to-JSON function"""


def class_to_json(obj):
    """Returns a dictionary rep of a simple data structure"""
    return obj.__dict__
