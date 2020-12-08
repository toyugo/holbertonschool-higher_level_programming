#!/usr/bin/python3

i = ord('z')
while i >= ord('a'):
    print("{:c}".format((i)), end="")
    i -= 1
    print("{:c}".format((i - 32)), end="")
    i -= 1
