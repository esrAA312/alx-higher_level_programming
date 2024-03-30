#!/usr/bin/python3
"""
handling HTTP errors
"""
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    X = argv[1]
    try:
        with request.urlopen(X) as re:
            be = re.read()
            print(be.decode('utf-8'))
    except error.HTTPError as err:
        print(f"Error code: {err.code}")

