#!/usr/bin/python3
"""
Module for my list class
"""


class MyList(list):
    """
    elements of the list int type
    return my list and sorted list
    """
    def print_sorted(self):
        '''Method for printing sorted list'''
        print(sorted(self))
