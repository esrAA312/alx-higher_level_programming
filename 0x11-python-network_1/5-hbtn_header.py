#!/usr/bin/python3
"""
sends a request and displays
"""
import requests
import sys

if __name__ == "__main__":
    Re = requests.get(sys.argv[1])
    he = Re.headers
    _Id = he.get("X-Request-Id")
    print(_Id)
