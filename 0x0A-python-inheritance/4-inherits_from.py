#!/usr/bin/python3
"""
Module to check if object is an instance of a
"""


def inherits_from(obj, a_class):
    """
    Check if an obj is a true subclass of a class.
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class) and type(obj) != a_class
