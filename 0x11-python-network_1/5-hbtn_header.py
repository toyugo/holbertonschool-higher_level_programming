#!/usr/bin/python3
""" Fetches """
import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    try:
        resp = requests.get(url)
    except requests.exceptions.RequestException:
        pass
    else:
        headtext = resp.headers
        print(headtext['X-Request-Id'])
