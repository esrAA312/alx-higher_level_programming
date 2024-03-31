#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response.
"""

from requests import post


def search(qee):
    """
    displays the body of the response.
    """

    URL = 'http://0.0.0.0:5000/search_user'
    De = {'q': qee}
    response = post(URL, De)

    tyee = response.headers['content-type']

    if tyee == 'application/json':
        result = response.json()
        _id = result.get('id')
        nee = result.get('name')
        if (result != {} and _id and nee):
            return "[{}] {}".format(_id, nee)
        else:
            return 'No result'
    else:
        return 'Not a valid JSON'


if __name__ == '__main__':
    from sys import argv

    qee = argv[1] if len(argv) >= 2 else ""
    print(search(qee))
