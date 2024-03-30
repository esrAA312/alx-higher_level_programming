#!/usr/bin/python3
"""
Sends a POST request"""


if __name__ == '__main__':
    from sys import argv
    from requests import post

    Ue = argv[1]
    Ee = argv[2]
    Re = post(Ue, {'email': Ee})
    print(Re.text)
