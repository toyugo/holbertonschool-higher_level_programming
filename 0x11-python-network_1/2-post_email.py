#!/usr/bin/python3
""" Module  to get url response """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]})
    data = data.encode('ascii')
    url = sys.argv[1]
    with open(urllib.request.urlopen(url, data)):
        print("Your email is : {}".format(response.info['email']))
