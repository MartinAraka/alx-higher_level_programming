#!/usr/bin/python3
"""this module defines a class square
that inherits from Rectangle"""

import json
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """takes in similar arguments to rectangle"/
        "replaces width and height with size"""
        super().__init__(size, size, x, y, id)
