#!/usr/bin/python3
"""github"""
import requests
import sys


def get_user_id(username, password):
    url = f"https://api.github.com/user"
    headers = {"Authorization": f"token {password}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        return user_data["id"]
    else:
        return None


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    user_id = get_user_id(username, password)
    print(user_id)
