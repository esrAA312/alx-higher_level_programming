#!/usr/bin/python3
"""
Python script that takes in a URL"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as ree:
        HT = ree.info()
        Eeget = HT.get('X-Request-Id')
        print(Eeget)
