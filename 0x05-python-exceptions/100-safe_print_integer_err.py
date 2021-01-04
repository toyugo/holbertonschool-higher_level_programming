#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format())
    except:
        return False
    else:
        return True
