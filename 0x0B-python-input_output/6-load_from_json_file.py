#!/usr/bin/python3
"""this module defines load from json file"""


def load_from_json_file(filename):
    """"create an object from a json file"""
    import json

    with open(file, encoding="utf=8") as file:
        return json.load(file)
