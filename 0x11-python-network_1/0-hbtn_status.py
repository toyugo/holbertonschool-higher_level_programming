#!/usr/bin/python3
import urllib.request as ur
""" Module """

if __name__ == "__main__":
    with ur.urlopen("https://intranet.hbtn.io/status") as resp:
        print(resp())
