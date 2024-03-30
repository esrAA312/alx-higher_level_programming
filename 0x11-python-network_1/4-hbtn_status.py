#!/usr/bin/python3
"""
fetche
"""

import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    re = requests.get(url)
    html = re.content

    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
