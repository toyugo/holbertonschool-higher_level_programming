#!/usr/bin/python3
""" Module  to get url response """
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(str(sys.argv[1])) as resp:
        a = resp.info()
    print("{}".format(a['X-Request-Id']))
