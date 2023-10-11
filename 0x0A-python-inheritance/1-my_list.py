#!/usr/bin/python3
"""MyList inherits from list"""


class MyList(list):
    """list subclass"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
