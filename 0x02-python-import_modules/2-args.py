#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    lenM = len(argv)
    i = 1
    if lenM - 1 != 1:
        print("{} arguments.".format(lenM - 1))
    else:
        print("1 argument")
    while i < lenM:
        print("{}: {}".format(i, argv[i]))
        i += 1
