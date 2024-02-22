#!/usr/bin/python3
"""this module defines a python class to JSON function"""

def class_to_json(obj):
    """"Returns dictionary representation of a simple structure"""
    return obj.__dict__
