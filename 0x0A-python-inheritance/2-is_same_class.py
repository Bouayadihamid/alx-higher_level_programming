#!/usr/bin/python3
"""
Module for same class method
"""


def is_same_class(obj, a_class):
    """
    object is the most base type class, a_class
    cointain instance of the object class
    """
    if (type(obj) == a_class):
        # the object is exactly an instance of the a_class
        return True
    # otherwise,
    return False
