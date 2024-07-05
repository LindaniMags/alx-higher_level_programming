#!/usr/bin/python3
""" If the HTTP status code is greater than or equal to 400, print: Error code """
import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(argv[1])
    status = response.status_code
    print(response.text) if status < 400 else print(
        f"Error code: {response.status_code}")
