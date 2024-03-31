#!/usr/bin/python3
"""github."""

import requests
import sys


def get_user_id(username, password):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, auth=(username, password))
    user_data = response.json()
    return user_data.get('id')


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    user_id = get_user_id(username, password)
    print(user_id)
