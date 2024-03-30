#!/usr/bin/python3
"""
displays the response body.
"""
from sys import argv
import requests


if __name__ == "__main__":
    uee = argv[1]

    ree = requests.get(uee)
    if ree.status_code >= 400:
        print("Error code: {}".format(ree.status_code))
    else:
        print(ree.text)
