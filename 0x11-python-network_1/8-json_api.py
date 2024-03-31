#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""

from requests import post


def suser(Q):
    """Sends a req."""
    Uee = 'http://0.0.0.0:5000/search_user'
    d = {'q': Q}
    response = post(Uee, d)

    te = response.headers['content-type']

    if te == 'application/json':
        result = response.json()
        u_d = result.get('id')
        ne = result.get('name')
        if result and u_d and ne:
            return "[{}] {}".format(u_d, ne)
        else:
            return 'No result'
    else:
        return 'Not a valid JSON'


if __name__ == '__main__':
    from sys import argv

    Q = argv[1] if len(argv) >= 2 else ""
    print(suser(Q))
