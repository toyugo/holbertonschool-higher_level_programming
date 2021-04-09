#!/usr/bin/python3
import urllib.request as ur
""" Module """

if __name__ == "__main__":
    with ur.urlopen("https://intranet.hbtn.io/status") as resp:
        a = resp.read()
    print("\t - type: {}".format(type(a)))       
    print("\t - content: {}".format(a))
    print("\t - utf8 content: {}".format(a.decode('utf-8')))
    