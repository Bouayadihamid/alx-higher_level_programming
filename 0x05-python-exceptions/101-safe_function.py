#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        var = fct(*args)
        return var
    except Exception as m:
        print("Exception: {}".format(m), file=sys.stderr)
        return None
