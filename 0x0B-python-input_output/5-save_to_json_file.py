#!/usr/bin/python3
"""module that defines a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an obj to a txt file using JSON format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
