#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except:
        print("Exception {}".format(sys.exc_info()[0]), file=sys.stderr)
        return False
    else:
        return True
