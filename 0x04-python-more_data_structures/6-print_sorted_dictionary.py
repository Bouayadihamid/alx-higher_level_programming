#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary.keys()):
        return ("{}: {}".format(i, a_dictionary[i]))
