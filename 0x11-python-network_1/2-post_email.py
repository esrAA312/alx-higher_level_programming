#!/usr/bin/python3
"""
Sends a POST request to a given URL with a given email.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    Ve = {"email": sys.argv[2]}
    De = urllib.parse.urlencode(Ve)
    De = data.encode("ascii")
    request = urllib.request.Request(url, De)
    with urllib.request.urlopen(request) as ree:
        Xe = ree.read().decode("utf-8")
        print(Xe)

