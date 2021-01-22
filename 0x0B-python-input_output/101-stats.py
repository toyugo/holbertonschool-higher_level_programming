#!/usr/bin/python3
""" Module to read the standard input """
import sys


def printDictionary(dict):
    """ print a dicitonary with specific format """
    for i in sorted(dict):
        print("{}: {}".format(i, dict[i]))
    # for i in dict.items():
    # print("{}: {}".format(i[0], i[1]))

if __name__ == "__main__":
    """ Main """
    cp = 1
    buffer = {}
    size = 0
    for line in sys.stdin:
        if cp == 10:
            print("File size: {:d}".format(size))
            printDictionary(buffer)
            buffer = {}
            cp = 1
        else:
            statusCode = line.split(' ')[7]
            size += int(line.split(' ')[8])
            try:
                buffer[statusCode]
                countCode = buffer[statusCode]
                buffer[statusCode] = countCode + 1
            except:
                buffer[statusCode] = 1
            cp += 1
    print("File size: {:d}".format(size))
    printDictionary(buffer)
