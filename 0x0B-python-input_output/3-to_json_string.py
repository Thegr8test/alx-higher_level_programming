#!/usr/bin/python3
"""
module that contains the JSON string
"""

import json


def to_json_string(my_obj):
    """returns the JSON rep of an object"""
    return json.dumps(my_obj)
