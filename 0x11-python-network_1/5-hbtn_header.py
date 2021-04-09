#!/usr/bin/python3
""" Fetches """
import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    resp = requests.get(url)
    if resp :
        headtext = resp.headers
        if headtext['X-Request-Id']:
            print(headtext['X-Request-Id'])
