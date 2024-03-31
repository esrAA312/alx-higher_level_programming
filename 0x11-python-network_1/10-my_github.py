#!/usr/bin/python3
""" GitHub"""
import requests
from sys import argv


def getide(Ue, Pe):
    Ue = f"https://api.github.com/user"
    headers = {"Authorization": f"token {Pe}"}
    response = requests.get(U, headers=headers)
    if response.status_code == 200:
        uu = response.json()
        if "id" in uu:
            return uu["id"]
    return None


if __name__ == "__main__":
    ne = argv[1]
    Pe = argv[2]

    ide = getide(Ue, Pe)
    print(ide)
