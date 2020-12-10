#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    lenM = len(argv)
    i = 1
    while i < lenM:
        print("{}: {}".format(i, argv[i]))
        i += 1
