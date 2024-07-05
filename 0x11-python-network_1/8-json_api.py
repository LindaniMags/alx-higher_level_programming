#!/usr/bin/python3
""" Sends a POST request to URL with a letter as a parameter. """
import requests
from sys import argv

if __name__ == '__main__':
    q = argv[1] if len(argv) == 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': q})
    try:
        r_json = r.json()
        id, name = r_json.get('id'), r_json.get('name')
        if len(r_json) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(r_json.get('id'), r_json.get('name')))
    except Exception:
        print("Not a valid JSON")
